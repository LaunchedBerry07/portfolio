#!/usr/bin/env python3
"""Render the shared static header/footer and apply Pass A design corrections.

The portfolio pages are static HTML (except the Jekyll-processed 404 page), so
this script keeps the reusable shell in one source and writes generated markup
into each published HTML file. Run from the repository root with:
    python3 scripts/render_shared_shell.py
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = Path('/home/ubuntu/projects/website-b0b457a3')
LOGO_SOURCE = PROJECT / 'f99d4b7c-0d1d-435a-acca-76a508620eac-1_all_316386.png'
LOGO_REL = Path('assets/images/brand/stephanie-nadeau-logo-horizontal.png')

NAV_TEMPLATE = '''<nav aria-label="Main navigation" class="site-nav">
  <a aria-label="Stéphanie Nadeau — home" class="site-nav__brand" href="{home}">
    <img class="site-nav__logo" src="{logo}" width="936" height="445" alt="" decoding="async">
  </a>
  <button aria-controls="primary-navigation" aria-expanded="false" aria-label="Open navigation menu" class="site-nav__toggle" type="button">
    <i aria-hidden="true" class="fa-solid fa-bars"></i><span>Menu</span>
  </button>
  <div class="site-nav__links" id="primary-navigation">
    <a{home_attrs} href="{home}">Home</a>
    <a{services_attrs} href="{services}">Services</a>
    <a{portfolio_attrs} href="{portfolio}">Portfolio</a>
    <a{technology_attrs} href="{technology}">Tech &amp; AI</a>
    <a{clients_attrs} href="{clients}">Clients &amp; Sectors</a>
    <a{profile_attrs} href="{profile}">Profile &amp; CV</a>
    <a class="site-nav__contact{contact_class}"{contact_current} href="{contact}"><i aria-hidden="true" class="fa-regular fa-envelope"></i><span>Get in touch</span></a>
  </div>
</nav>'''

FOOTER_TEMPLATE = '''<footer class="site-footer" id="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__identity">
      <a class="site-footer__brand" href="{home}">Stéphanie Nadeau</a>
      <p>Language expertise, supported by technology.</p>
      <a class="site-footer__email" href="mailto:snadeau.tran@gmail.com">snadeau.tran@gmail.com</a>
    </div>
    <nav class="site-footer__nav" aria-label="Footer navigation">
      <a href="{home}">Home</a>
      <a href="{services}">Services</a>
      <a href="{portfolio}">Portfolio</a>
      <a href="{technology}">Tech &amp; AI</a>
      <a href="{clients}">Clients &amp; Sectors</a>
      <a href="{profile}">Profile &amp; CV</a>
      <a href="{contact}">Contact</a>
    </nav>
    <div class="site-footer__social"><a href="https://linkedin.com/in/s-nadeau" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i><span>LinkedIn</span></a></div>
  </div>
  <div class="site-footer__bottom"><span>© <span class="current-year"></span> Stéphanie Nadeau. All rights reserved.</span><a href="#top">Back to top ↑</a></div>
</footer>'''


def current_attrs(is_current: bool, exact: bool = True) -> str:
    if not is_current:
        return ''
    state = 'page' if exact else 'location'
    return f' class="is-current" aria-current="{state}"'


def page_shell(rel: Path) -> tuple[str, str]:
    page_dir = rel.parent
    depth = 0 if str(page_dir) == '.' else len(page_dir.parts)
    prefix = '../' * depth
    routes = {
        'home': prefix + 'index.html',
        'services': prefix + 'services/',
        'portfolio': prefix + 'portfolio/linguistic-case-studies/',
        'technology': prefix + 'portfolio/technical-projects/',
        'clients': prefix + 'clients-sectors/',
        'profile': prefix + 'profile/',
        'contact': prefix + 'contact/',
        'logo': prefix + LOGO_REL.as_posix(),
    }
    key = None
    exact = True
    path = rel.as_posix()
    if path == 'index.html':
        key = 'home'
    elif path.startswith('services/'):
        key = 'services'
    elif path.startswith('portfolio/linguistic-case-studies/'):
        key = 'portfolio'
        exact = path == 'portfolio/linguistic-case-studies/index.html'
    elif path.startswith('portfolio/technical-projects/'):
        key = 'technology'
        exact = path == 'portfolio/technical-projects/index.html'
    elif path.startswith('clients-sectors/'):
        key = 'clients'
    elif path.startswith('profile/'):
        key = 'profile'
    elif path.startswith('contact/'):
        key = 'contact'

    values = dict(routes)
    for name in ('home', 'services', 'portfolio', 'technology', 'clients', 'profile'):
        values[name + '_attrs'] = current_attrs(key == name, exact)
    values['contact_class'] = ' is-current' if key == 'contact' else ''
    values['contact_current'] = f' aria-current="{"page" if exact else "location"}"' if key == 'contact' else ''
    nav = NAV_TEMPLATE.format(**values)
    footer = FOOTER_TEMPLATE.format(**routes)
    return nav, footer


def replace_single_shell(text: str, tag: str, class_name: str, replacement: str, rel: Path) -> str:
    pattern = re.compile(rf'<{tag}\b[^>]*>.*?</{tag}\s*>', re.IGNORECASE | re.DOTALL)
    matches = [m for m in pattern.finditer(text) if re.search(r'\bclass\s*=\s*(["\'])[^"\']*\b' + re.escape(class_name) + r'\b[^"\']*\1', m.group(0), re.I)]
    if len(matches) != 1:
        raise RuntimeError(f'{rel}: expected exactly one {tag}.{class_name}, found {len(matches)}')
    match = matches[0]
    return text[:match.start()] + replacement + text[match.end():]


def add_small_organic_frames(text: str) -> str:
    """Make outlined compact labels irregular without changing pills or circles."""
    tag_pattern = re.compile(r'<(span|div)\b[^>]*\bclass\s*=\s*(["\'])(.*?)\2[^>]*>', re.I | re.S)

    def add(match: re.Match[str]) -> str:
        classes = match.group(3).split()
        full_border = 'border' in classes or any(re.fullmatch(r'border-\d+', item) for item in classes)
        organic = any(item.startswith('organic-border') or item == 'organic-frame--small' for item in classes)
        compact_corner = 'rounded-sm' in classes or 'rounded' in classes
        pill = any(item == 'rounded-full' or item.startswith('rounded-t-') or item.startswith('rounded-b-') or item.startswith('rounded-l-') or item.startswith('rounded-r-') for item in classes)
        if full_border and compact_corner and not organic and not pill:
            before = match.group(0)
            updated = match.group(3) + ' organic-frame--small'
            return before.replace(match.group(3), updated, 1)
        return match.group(0)

    return tag_pattern.sub(add, text)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 0 and new in text:
        return text
    if count != 1:
        raise RuntimeError(f'{label}: expected one occurrence, found {count}')
    return text.replace(old, new, 1)


def inline_negative_heading_icons(text: str, label: str) -> str:
    pattern = re.compile(
        r'<h2\b[^>]*\bclass="([^"]*)"[^>]*>(.*?)<i\b[^>]*\bclass="([^"]*)"[^>]*></i>(.*?)</h2>',
        re.I | re.S,
    )
    matches = [m for m in pattern.finditer(text) if 'absolute' in m.group(3).split() and '-left-8' in m.group(3).split()]
    if not matches:
        return text
    for match in reversed(matches):
        heading_classes = [c for c in match.group(1).split() if c not in {'relative', 'inline-block'}]
        icon_classes = [c for c in match.group(3).split() if c not in {'absolute', '-top-3', '-top-4', '-left-8'}]
        for c in ('inline-block', 'ml-2', 'align-middle', 'text-lg'):
            if c not in icon_classes:
                icon_classes.append(c)
        icon = f'<i aria-hidden="true" class="{" ".join(icon_classes)}"></i>'
        replacement = f'<h2 class="{" ".join(heading_classes)}">{match.group(2)}{icon}{match.group(4)}</h2>'
        text = text[:match.start()] + replacement + text[match.end():]
    return text


def apply_pass_a_css() -> None:
    site = ROOT / 'assets/css/site.css'
    text = site.read_text()
    text = replace_once(text, '.site-nav__mark { width:3rem; height:3rem; position:relative; display:grid; place-items:center; border:2px solid var(--navy); border-radius:50%; background:var(--mist); font-family:"Playfair Display",serif; font-weight:700; font-size:1.25rem; }', '.site-nav__logo { display:block; width:auto; height:3.35rem; max-width:min(100%,12.5rem); object-fit:contain; }', 'logo header')
    text = replace_once(text, '.site-nav__mark-cross::before,.site-nav__mark-cross::after { content:""; position:absolute; background:var(--turquoise); opacity:.8; }\n\n.site-nav__mark-cross::before { width:100%; height:1px; left:0; top:50%; }\n\n.site-nav__mark-cross::after { height:100%; width:1px; top:0; left:50%; }\n\n.site-nav__brand-copy { display:flex; flex-direction:column; line-height:1.15; }\n\n.site-nav__name { font-family:"Playfair Display",serif; font-weight:700; font-size:1.1rem; }\n\n.site-nav__tagline { margin-top:.25rem; color:var(--sky); text-transform:uppercase; letter-spacing:.13em; font-size:.62rem; }', '', 'remove CSS-drawn logo and old wordmark styles')
    text = replace_once(text, ':root { color-scheme: light; --navy:#13293D; --darkpink:#D14D72; --bluegreen:#087E8B; --turquoise:#149E92; --seafoam:#83E0D0; --mist:#EAF4F8; --sky:#5B96BD; --page:#FAFCFD; }', ':root { color-scheme: light; --navy:#13293D; --darkpink:#D14D72; --bluegreen:#087E8B; --turquoise:#149E92; --seafoam:#83E0D0; --mist:#EAF4F8; --sky:#5B96BD; --page:#FAFCFD; --radius-organic:2.4rem .9rem 2.1rem 1.1rem / 1rem 2rem .9rem 2.3rem; --radius-organic-small:1.15rem .4rem .95rem .45rem / .4rem .95rem .45rem 1.15rem; }\n\n.organic-frame { border-radius:var(--radius-organic); }\n.organic-frame--small { border-radius:var(--radius-organic-small); }', 'shared organic radii')
    if '.assignment-card__image { border-radius:var(--radius-organic-small); }' not in text:
        text = text.replace('.organic-frame--small { border-radius:var(--radius-organic-small); }', '.organic-frame--small { border-radius:var(--radius-organic-small); }\n.assignment-card__image { border-radius:var(--radius-organic-small); }')
    text = replace_once(text, '.service-jump-nav__inner { background:#fff; border:2px solid var(--bluegreen); border-radius:1rem; padding:1.15rem 1.35rem; box-shadow:4px 4px 0 var(--seafoam); }', '.service-jump-nav__inner { background:#fff; border:2px solid var(--bluegreen); border-radius:var(--radius-organic); padding:1.15rem 1.35rem; box-shadow:4px 4px 0 var(--seafoam); }', 'organic service jump frame')
    text = replace_once(text, '.home-hero__image { display:block; width:145%; max-width:none; height:auto; max-height:none; margin-left:0; transform:translateY(-1.25rem); object-fit:contain; border:0; border-radius:0; box-shadow:none; }', '.home-hero__image { display:block; width:100%; max-width:100%; height:auto; max-height:none; margin-left:0; transform:translateY(-1.25rem); object-fit:contain; border:0; border-radius:0; box-shadow:none; }', 'home hero illustration clearance')
    text = text.replace('.home-hero__image { width:100%; max-width:100%; max-height:none; margin-left:0; transform:none; }', '.home-hero__image { width:100%; max-width:100%; max-height:none; margin-left:0; transform:none; }')
    site.write_text(text)

    css_changes = {
        'assets/css/404.css': [('.error-art__stamp {', '.error-art__stamp {\n  border-radius:var(--radius-organic-small);')],
        'assets/css/clients-sectors.css': [
            ('.cs-hero__visual { position:relative; min-width:0; aspect-ratio:1.22 / 1; overflow:hidden; border-radius:1rem;', '.cs-hero__visual { position:relative; min-width:0; aspect-ratio:1.22 / 1; overflow:hidden; border-radius:var(--radius-organic);'),
            ('border-radius:1.15rem .45rem 1rem .5rem;', 'border-radius:var(--radius-organic);'),
            ('border-radius:1.2rem; background:var(--cs-navy);', 'border-radius:var(--radius-organic); background:var(--cs-navy);'),
            ('border-radius:1rem; background:linear-gradient(110deg,#EAF4F8,#F5FAFB);', 'border-radius:var(--radius-organic); background:linear-gradient(110deg,#EAF4F8,#F5FAFB);'),
        ],
        'assets/css/contact.css': [('border-radius:.8rem;', 'border-radius:var(--radius-organic);')],
        'assets/css/portfolio.css': [
            ('border-radius:3px;', 'border-radius:var(--radius-organic-small);'),
            ('.portfolio-volume-note { margin:0 auto; max-width:48rem; padding:1rem 1.25rem; border-left:3px solid #087E8B; background:#EAF4F8;', '.portfolio-volume-note { margin:0 auto; max-width:48rem; padding:1rem 1.25rem; border:1px solid #087E8B; border-left-width:3px; border-radius:var(--radius-organic); background:#EAF4F8;'),
        ],
        'assets/css/profile.css': [
            ('border-left:3px solid var(--turquoise); background:var(--mist);', 'border:1px solid rgba(20,158,146,.45); border-left:3px solid var(--turquoise); border-radius:var(--radius-organic); background:var(--mist);'),
            ('border-radius: 4px;', 'border-radius:var(--radius-organic-small);'),
            ('border-radius: 4px 12px 5px 10px;', 'border-radius:var(--radius-organic);'),
            ('border-radius: 5px 14px 6px 12px;', 'border-radius:var(--radius-organic-small);'),
            ('border-radius: 6px 16px 7px 13px;', 'border-radius:var(--radius-organic);'),
        ],
        'assets/css/services.css': [
            ('border-radius:1.25rem .45rem 1rem .5rem;', 'border-radius:var(--radius-organic);'),
            ('border-radius:1rem .4rem 1rem .4rem;', 'border-radius:var(--radius-organic);'),
            ('border-radius:1rem .45rem 1rem .45rem;', 'border-radius:var(--radius-organic);'),
            ('border-radius:1rem .35rem 1rem .35rem;', 'border-radius:var(--radius-organic);'),
            ('.svc-terms { margin-top:1.4rem; padding:1.5rem 1.7rem; border-left:3px solid var(--svc-turquoise); background:#F5FAFB; }', '.svc-terms { margin-top:1.4rem; padding:1.5rem 1.7rem; border:1px solid #D6E7EA; border-left:3px solid var(--svc-turquoise); border-radius:var(--radius-organic); background:#F5FAFB; }'),
        ],
        'assets/css/technical-projects.css': [
            ('.tech-method { background:#EAF4F8;border-radius:1.25rem; }', '.tech-method { background:#EAF4F8;border-radius:var(--radius-organic); }'),
            ('.tech-method-grid article { background:#fff;border:1px solid rgba(19,41,61,.10);border-radius:1rem;padding:1.25rem; }', '.tech-method-grid article { background:#fff;border:1px solid rgba(19,41,61,.10);border-radius:var(--radius-organic);padding:1.25rem; }'),
        ],
    }
    for rel, replacements in css_changes.items():
        fp = ROOT / rel
        content = fp.read_text()
        for old, new in replacements:
            if old not in content and new in content:
                continue
            if old not in content:
                raise RuntimeError(f'{rel}: expected CSS fragment not found: {old[:70]}')
            content = content.replace(old, new)
        fp.write_text(content)

    # Image frames on the home page and compact career cards should not use geometric corners.
    home_css = ROOT / 'assets/css/site.css'
    content = home_css.read_text()
    content = content.replace('.home-hero__image {', '.home-hero__image {', 1)
    home_css.write_text(content)


def apply_targeted_html() -> None:
    # Store and use the supplied unmodified official horizontal logo.
    logo_path = ROOT / LOGO_REL
    logo_path.parent.mkdir(parents=True, exist_ok=True)
    if not logo_path.exists():
        shutil.copy2(LOGO_SOURCE, logo_path)

    for fp in sorted(ROOT.rglob('*.html')):
        rel = fp.relative_to(ROOT)
        text = fp.read_text()
        nav, footer = page_shell(rel)
        text = replace_single_shell(text, 'nav', 'site-nav', nav, rel)
        text = replace_single_shell(text, 'footer', 'site-footer', footer, rel)
        text = add_small_organic_frames(text)
        fp.write_text(text)

    # Clip-prone decorations become in-flow labels, and heading icons sit beside their text.
    polaris = ROOT / 'portfolio/linguistic-case-studies/polaris-industries.html'
    text = polaris.read_text()
    text = replace_once(text, '<div aria-hidden="true" class="absolute -top-8 -left-6 transform -rotate-12 text-darkpink font-hand text-2xl hidden md:block">Multi-batch! <i class="fa-solid fa-arrow-turn-down ml-1 text-sm"></i></div>', '<div aria-hidden="true" class="inline-flex items-center gap-2 mb-4 transform -rotate-2 text-darkpink font-hand text-2xl hidden md:block">Multi-batch! <i class="fa-solid fa-arrow-turn-down text-sm"></i></div>', 'Polaris clipped annotation')
    polaris.write_text(text)

    # The image mask was clipping a 145%-width hero illustration. The stylesheet now fits it to its column.
    # Keep two content icons in the home hero heading fully within its frame.
    home = ROOT / 'index.html'
    text = home.read_text()
    text = text.replace('absolute -top-4 -left-6 text-3xl text-seafoam opacity-50', 'absolute -top-4 -left-2 text-3xl text-seafoam opacity-50')
    home.write_text(text)

    # Remove out-of-box absolute title icons from Caifan and DataBerry Nexus; keep them inline with safe spacing.
    for rel, label in [
        ('portfolio/technical-projects/caifan.html', 'Caifan heading layout'),
        ('portfolio/technical-projects/databerry-nexus.html', 'DataBerry Nexus heading layout'),
        ('portfolio/technical-projects/databerry.html', 'DataBerry Manager heading layout'),
        ('portfolio/technical-projects/email-solicitation-filtering.html', 'Email filtering heading layout'),
    ]:
        fp = ROOT / rel
        text = fp.read_text()
        text = inline_negative_heading_icons(text, label)
        fp.write_text(text)

    # Small bordered labels and annotations use the shared organic frame shape; avoid the button family.
    for rel in [
        'portfolio/linguistic-case-studies/federation-adventiste.html',
        'portfolio/linguistic-case-studies/thomson-technology.html',
    ]:
        fp = ROOT / rel
        text = fp.read_text()
        text = re.sub(r'(class="[^"]*\bborder\b[^"]*\brounded\b[^"]*)', lambda m: m.group(1) if 'organic-frame--small' in m.group(1) else m.group(1) + ' organic-frame--small', text)
        fp.write_text(text)

    # Explicit framed evidence/callout notes and side-rule notes that are documented in the audit.
    note_targets = {
        'portfolio/linguistic-case-studies/us-bank.html': [('rounded-r-md', 'organic-frame')],
        'portfolio/linguistic-case-studies/wsp-global.html': [('rounded-r-md', 'organic-frame')],
        'portfolio/technical-projects/databerry.html': [('border-l-4 border-mist pl-4', 'border border-mist border-l-4 pl-4 organic-frame--small')],
        'portfolio/technical-projects/databerry-nexus.html': [('border-l-4 border-mist pl-4', 'border border-mist border-l-4 pl-4 organic-frame--small')],
        'portfolio/technical-projects/caifan.html': [('border-l-4 border-mist pl-4', 'border border-mist border-l-4 pl-4 organic-frame--small')],
        'portfolio/technical-projects/email-solicitation-filtering.html': [('border-l-4 border-mist pl-4', 'border border-mist border-l-4 pl-4 organic-frame--small')],
        'portfolio/technical-projects/databerry.html': [('border-l-2 border-gray-200', 'border border-gray-200 border-l-2 organic-frame--small')],
        'portfolio/technical-projects/llm-prompt-engineering.html': [('rounded-r-md', 'organic-frame')],
    }
    for rel, pairs in note_targets.items():
        fp = ROOT / rel
        text = fp.read_text()
        for old, new in pairs:
            if old in text and new not in text:
                # Restrict broad class substitution to elements with a bordered note shape.
                if old == 'rounded-r-md':
                    text = re.sub(r'(class="[^"]*\bborder\b[^"]*\b)' + re.escape(old) + r'\b([^"]*)', r'\1' + new + r'\2', text, count=1)
                else:
                    text = replace_once(text, old, new, f'{rel} callout frame')
        fp.write_text(text)


def main() -> None:
    html_files = sorted(ROOT.rglob('*.html'))
    if len(html_files) != 28:
        raise RuntimeError(f'Expected the audited 28 HTML pages, found {len(html_files)}')
    apply_pass_a_css()
    apply_targeted_html()
    print(f'Pass A updated {len(html_files)} HTML pages plus shared/page CSS in {ROOT}')


if __name__ == '__main__':
    main()
