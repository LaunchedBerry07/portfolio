from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HTML_LINK = re.compile(r"<a\b[^>]*>.*?</a\s*>", re.IGNORECASE | re.DOTALL)
OPENING_A = re.compile(r"^<a\b[^>]*>", re.IGNORECASE | re.DOTALL)
CLASS_ATTR = re.compile(r"(\bclass\s*=\s*)(['\"])(.*?)\2", re.IGNORECASE | re.DOTALL)

PRIMARY_TOKENS = {
    "cta--primary",
    "contact-action--primary",
    "home-cta__button",
    "profile-button",
    "site-nav__contact",
    "svc-button--primary",
    "svc-button--pink",
    "tech-contact__link",
    "error-home-button",
}
SECONDARY_TOKENS = {
    "cta--secondary",
    "contact-action--secondary",
    "svc-button--outline",
    "profile-button--outline",
}
SKIP_TOKENS = {"skip-link", "error-skip-link", "visually-hidden"}
LAYOUT_PREFIXES = (
    "inline-flex", "inline-block", "items-", "justify-", "gap-", "text-xs", "text-sm",
    "text-base", "mb-", "mt-", "ml-", "mr-", "transition-",
)


def class_value(tag) -> list[str]:
    value = tag.get("class", [])
    return value if isinstance(value, list) else str(value).split()


def class_attribute(tag_text: str, classes: list[str]) -> str:
    opening = OPENING_A.match(tag_text)
    if not opening:
        raise ValueError("Could not locate <a> opening tag")
    start = opening.group(0)
    value = " ".join(dict.fromkeys(classes))
    match = CLASS_ATTR.search(start)
    if match:
        updated = CLASS_ATTR.sub(lambda m: f'{m.group(1)}{m.group(2)}{value}{m.group(2)}', start, count=1)
    else:
        updated = start[:-1] + f' class="{value}">'
    return updated + tag_text[len(start):]


def is_shell_or_local_navigation(anchor) -> bool:
    if anchor.find_parent(class_="site-nav") and "site-nav__contact" not in class_value(anchor):
        return True
    if anchor.find_parent("footer"):
        return True
    if anchor.find_parent(class_="service-jump-nav") or anchor.find_parent(class_="svc-jump"):
        return True
    return False


def is_skip_link(classes: list[str]) -> bool:
    return bool(set(classes) & SKIP_TOKENS)


def role_for(anchor, classes: list[str], text: str) -> str | None:
    tokens = set(classes)
    if tokens & SECONDARY_TOKENS:
        return "secondary"
    if tokens & PRIMARY_TOKENS:
        return "primary"
    # Preserve the established visual role of the two homepage hero actions and
    # the repeated CTA pair on technical-project detail pages while replacing
    # their page-specific presentation classes.
    if {"organic-border", "bg-navy", "text-white"}.issubset(tokens):
        return "primary"
    if "bg-white" in tokens and ({"organic-border", "organic-border-pink"} & tokens):
        return "secondary"
    if {"organic-border-pink", "bg-darkpink", "text-white"}.issubset(tokens):
        return "primary"
    # A text-only fallback catches future project-contact prompts without
    # misclassifying equal-weight destination links such as the 404 suggestions.
    if text.casefold().startswith("discuss "):
        return "primary"
    return None


def dark_context(anchor, classes: list[str]) -> bool:
    if set(classes) & {"text-white", "text-seafoam", "svc-text-link--light", "content-link--light"}:
        return True
    dark_tokens = {"bg-navy", "home-cta", "svc-final-cta", "svc-tech", "tech-hero", "portfolio-hero"}
    for parent in anchor.parents:
        parent_classes = set(class_value(parent)) if getattr(parent, "attrs", None) else set()
        if parent_classes & dark_tokens:
            return True
    return False


def content_classes(classes: list[str], light: bool) -> list[str]:
    # Keep only layout/size helpers; color, weight, underline and hover styles
    # are intentionally owned by the shared content-link component.
    kept = [c for c in classes if c == "svc-text-link" or c.startswith(LAYOUT_PREFIXES)]
    kept.extend(["content-link"])
    if light:
        kept.append("content-link--light")
    return list(dict.fromkeys(kept))


def normalize_html(path: Path) -> Counter:
    source = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(source, "html.parser")
    anchors = soup.find_all("a")
    matches = list(HTML_LINK.finditer(source))
    if len(anchors) != len(matches):
        raise RuntimeError(f"Anchor count mismatch in {path}: parsed={len(anchors)} raw={len(matches)}")

    counts: Counter = Counter()
    replacements = []
    for anchor, match in zip(anchors, matches):
        old_classes = class_value(anchor)
        if is_shell_or_local_navigation(anchor) or is_skip_link(old_classes):
            continue

        text = " ".join(anchor.stripped_strings)
        role = role_for(anchor, old_classes, text)
        if role:
            new_classes = ["cta", f"cta--{role}"]
            if "site-nav__contact" in old_classes:
                new_classes.append("site-nav__contact")
            if "is-current" in old_classes:
                new_classes.append("is-current")
            counts[f"cta--{role}"] += 1
        elif text or anchor.get("aria-label"):
            new_classes = content_classes(old_classes, dark_context(anchor, old_classes))
            counts["content-link" if "content-link--light" not in new_classes else "content-link--light"] += 1
        else:
            # Image-only links retain their existing behavior; no such links were
            # found in the audited pages, but leave them untouched if introduced.
            continue

        updated = class_attribute(match.group(0), new_classes)
        if updated != match.group(0):
            replacements.append((match.start(), match.end(), updated))

    for start, end, updated in reversed(replacements):
        source = source[:start] + updated + source[end:]
    if replacements:
        path.write_text(source, encoding="utf-8")
    counts["anchors-updated"] += len(replacements)
    return counts


def remove_rule(css: str, selector: str) -> str:
    pattern = re.compile(r"(?m)^" + re.escape(selector) + r"\s*\{[^{}]*\}\s*")
    return pattern.sub("", css)


def replace_rule(css: str, selector: str, body: str) -> str:
    pattern = re.compile(r"(?m)^" + re.escape(selector) + r"\s*\{[^{}]*\}")
    replacement = selector + " {\n" + body.rstrip() + "\n}"
    updated, count = pattern.subn(lambda _: replacement, css, count=1)
    if count != 1:
        raise RuntimeError(f"Expected one CSS rule for {selector}; found {count}")
    return updated


def clean_local_css() -> None:
    # The persistent header contact action shares the primary CTA skin; retain
    # only its compact layout and page-current indicator.
    path = ROOT / "assets/css/site.css"
    css = path.read_text()
    css = replace_rule(css, ".site-nav__contact", "  flex-shrink: 0;")
    css = remove_rule(css, ".site-nav__contact:hover")
    css = remove_rule(css, '.site-nav__contact[aria-current="page"]')
    css = css.replace(
        ".site-nav__contact { padding:.6rem .75rem; }",
        ".site-nav__contact.cta.cta--primary { min-height:2.65rem; padding:.55rem .7rem; font-size:.78rem; }",
    )
    active_selector = '.site-nav__contact.cta.cta--primary[aria-current="page"]'
    if active_selector not in css:
        css += f"\n{active_selector} {{ box-shadow: 4px 4px 0 var(--darkpink); }}\n"
    path.write_text(css)

    # 404: CTA colors and destination-link typography move to the shared roles.
    path = ROOT / "assets/css/404.css"
    css = path.read_text()
    for selector in (".error-home-button", ".error-home-button:hover"):
        css = remove_rule(css, selector)
    css = css.replace(".error-home-button:focus-visible,\n", "")
    css = re.sub(
        r"(?m)^\s*\.error-home-button\s*\{\s*width:\s*100%;\s*\}\s*",
        "  .error-actions .cta { width: 100%; }\n",
        css,
    )
    css = re.sub(
        r"@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\.error-home-button\s*\{[^{}]*\}\s*\}\s*",
        "",
        css,
    )
    css = replace_rule(
        css,
        ".error-destinations__links a",
        "  display: inline-flex;\n  align-items: center;\n  gap: .35rem;\n  min-height: 2rem;",
    )
    css = remove_rule(css, ".error-destinations__links a:hover")
    path.write_text(css)

    # Contact: the actions now get all visual states from .cta.
    path = ROOT / "assets/css/contact.css"
    css = path.read_text()
    for selector in (
        ".contact-action", ".contact-action--primary", ".contact-action--primary:hover",
        ".contact-action--secondary", ".contact-action--secondary i", ".contact-action--secondary:hover",
    ):
        css = remove_rule(css, selector)
    path.write_text(css)

    # Homepage: remove its bespoke CTA skin; the dark-banner context remains.
    path = ROOT / "assets/css/site.css"
    css = path.read_text()
    for selector in (".home-cta__button", ".home-cta__button:hover", ".home-cta__button:focus-visible"):
        css = remove_rule(css, selector)
    css = re.sub(r"@media\s*\(prefers-reduced-motion:reduce\)\s*\{\s*\.home-cta__button\s*\{[^{}]*\}\s*\}\s*", "", css)
    path.write_text(css)

    # Profile: remove primary/outline-specific skins.
    path = ROOT / "assets/css/profile.css"
    css = path.read_text()
    for selector in (".profile-button", ".profile-button:hover", ".profile-button--outline", ".profile-button--outline:hover"):
        css = remove_rule(css, selector)
    css = css.replace(".profile-button { width:100%; }", ".profile-hero__actions .cta { width:100%; }")
    css = css.replace(".profile-button,.profile-path-card { transition:none; }", ".profile-path-card { transition:none; }")
    css = css.replace(".profile-button:hover,.profile-path-card:hover { transform:none; }", ".profile-path-card:hover { transform:none; }")
    path.write_text(css)

    # Services: keep only the layout helper for inline links; all color and
    # typography now come from .content-link. CTA layout/skins are shared.
    path = ROOT / "assets/css/services.css"
    css = path.read_text()
    for selector in (
        ".svc-button", ".svc-button:hover", ".svc-button--primary", ".svc-button--primary:hover",
        ".svc-button--outline", ".svc-button--outline:hover", ".svc-button--pink", ".svc-button--pink:hover",
    ):
        css = remove_rule(css, selector)
    css = replace_rule(
        css,
        ".svc-text-link",
        "  display: inline-flex;\n  align-items: center;\n  gap: .45rem;",
    )
    css = remove_rule(css, ".svc-text-link--light")
    if ".svc-final-cta .cta {" not in css:
        css += "\n/* Page layout only; CTA appearance is defined by the shared role variants. */\n.svc-final-cta .cta { margin-top: .6rem; }\n"
    path.write_text(css)

    # Technical project index and contact: let the semantic role own link and CTA styling.
    path = ROOT / "assets/css/technical-projects.css"
    css = path.read_text()
    css = replace_rule(css, ".tech-project-card a", "  margin-top: auto;")
    css = remove_rule(css, ".tech-project-card a:hover")
    css = remove_rule(css, ".tech-project-card a:focus-visible")
    for selector in (".tech-contact__link", ".tech-contact__link:hover", ".tech-contact__link:focus-visible"):
        css = remove_rule(css, selector)
    path.write_text(css)


def append_shared_css() -> None:
    path = ROOT / "assets/css/site.css"
    css = path.read_text()
    marker = "/* Shared semantic CTA and content-link roles (limited pass B). */"
    if marker in css:
        motion_rule = """
@media (prefers-reduced-motion: reduce) {
  a.cta.cta--primary:hover,
  a.cta.cta--secondary:hover { transform: none; }
}
"""
        if "a.cta.cta--primary:hover,\n  a.cta.cta--secondary:hover" not in css:
            path.write_text(css + motion_rule)
        return
    css += """

/* Shared semantic CTA and content-link roles (limited pass B). */
a.cta.cta--primary,
a.cta.cta--secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .6rem;
  max-width: 100%;
  min-height: 3rem;
  padding: .75rem 1.2rem;
  border: 2px solid transparent;
  border-radius: var(--radius-organic-small);
  font: 700 .9rem/1.35 "Inter", sans-serif;
  text-align: center;
  text-decoration: none;
  transition: background-color .18s ease, color .18s ease, border-color .18s ease, box-shadow .18s ease, transform .18s ease;
}

a.cta.cta--primary,
a.cta.cta--primary:visited {
  border-color: var(--navy);
  background: var(--navy);
  box-shadow: 4px 4px 0 var(--seafoam);
  color: #fff;
}

a.cta.cta--primary:hover {
  transform: translate(-1px, -1px);
  box-shadow: 5px 5px 0 var(--darkpink);
}

a.cta.cta--secondary,
a.cta.cta--secondary:visited {
  border-color: var(--navy);
  background: #fff;
  box-shadow: 4px 4px 0 var(--darkpink);
  color: var(--navy);
}

a.cta.cta--secondary:hover {
  transform: translate(-1px, -1px);
  background: var(--mist);
  box-shadow: 5px 5px 0 var(--navy);
}

a.cta.cta--primary:active,
a.cta.cta--secondary:active {
  transform: translate(1px, 1px);
  box-shadow: 1px 1px 0 currentColor;
}

a.cta.cta--primary:focus-visible,
a.cta.cta--secondary:focus-visible,
a.content-link.content-link:focus-visible {
  outline: 3px solid var(--turquoise);
  outline-offset: 3px;
}

a.cta[aria-disabled="true"] {
  cursor: not-allowed;
  opacity: .55;
  pointer-events: none;
  transform: none;
  box-shadow: none;
}

a.content-link.content-link,
a.content-link.content-link:visited {
  color: var(--navy);
  font-weight: 600;
  text-decoration: underline;
  text-decoration-color: var(--turquoise);
  text-decoration-thickness: .1em;
  text-underline-offset: .2em;
  transition: color .18s ease, text-decoration-color .18s ease;
}

a.content-link.content-link:hover {
  color: var(--bluegreen);
  text-decoration-color: currentColor;
}

a.content-link.content-link--light,
a.content-link.content-link--light:visited {
  color: #fff;
  text-decoration-color: var(--seafoam);
}

a.content-link.content-link--light:hover {
  color: var(--seafoam);
  text-decoration-color: currentColor;
}

a.content-link[aria-disabled="true"] {
  cursor: not-allowed;
  opacity: .55;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  a.cta.cta--primary:hover,
  a.cta.cta--secondary:hover { transform: none; }
}
"""
    path.write_text(css)


def main() -> None:
    counts: Counter = Counter()
    html_files = sorted(ROOT.rglob("*.html"))
    for path in html_files:
        counts.update(normalize_html(path))
    clean_local_css()
    append_shared_css()
    print(f"HTML pages processed: {len(html_files)}")
    for key, value in sorted(counts.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
