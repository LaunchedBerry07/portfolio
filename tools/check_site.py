#!/usr/bin/env python3
"""Small standard-library checks for the static portfolio prototype."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.images = []
        self.stylesheets = []
        self.scripts = []
        self.service_cards = 0
        self.h1 = 0
        self.html_lang = None
        self.current_classes = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.html_lang = attrs.get("lang")
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append((attrs.get("src", ""), attrs.get("alt")))
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs.get("href", ""))
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        if tag == "article" and "service-card" in attrs.get("class", "").split():
            self.service_cards += 1
        if tag == "h1":
            self.h1 += 1


def fail(message):
    print("FAIL:", message)
    return False


def main():
    source = HTML.read_text(encoding="utf-8")
    parser = AuditParser()
    parser.feed(source)
    errors = []
    if parser.html_lang != "en": errors.append("HTML language is not en")
    if parser.h1 != 1: errors.append(f"expected one h1, found {parser.h1}")
    if parser.service_cards != 6: errors.append(f"expected six service cards, found {parser.service_cards}")
    required = ["Data Annotation", "Entry-level text and data labelling, guided by explicit instructions.", "Audience", "Context", "Terminology", "Purpose"]
    for phrase in required:
        if phrase not in source: errors.append(f"missing required text: {phrase}")
    for href in parser.links:
        if href.startswith("#") and href[1:] not in parser.ids:
            errors.append(f"broken in-page link: {href}")
        elif href and not re.match(r"^(?:https?://|mailto:|tel:|#)", href):
            if not (ROOT / href.split("#", 1)[0]).is_file():
                errors.append(f"missing local link target: {href}")
    for src, alt in parser.images:
        if alt is None: errors.append(f"image missing alt attribute: {src}")
        if not (ROOT / src).is_file(): errors.append(f"missing image: {src}")
    for src in parser.stylesheets + parser.scripts:
        if re.match(r"^https?://", src): errors.append(f"external runtime dependency: {src}")
        elif not (ROOT / src).is_file(): errors.append(f"missing local code resource: {src}")
    manifest = ROOT / "manus-routes.json"
    if not manifest.is_file(): errors.append("missing manus-routes.json")
    if errors:
        for error in errors: print("FAIL:", error)
        return 1
    print(f"PASS: lang=en, one h1, {parser.service_cards} service cards, internal links, local media/code and route manifest.")
    print(f"Checked {len(parser.links)} linked elements and {len(parser.images)} images.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
