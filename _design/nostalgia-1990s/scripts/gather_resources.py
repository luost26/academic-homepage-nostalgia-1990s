#!/usr/bin/env python3
"""Gather a pinned, uninstalled design-reference kit; never touch site files."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import hashlib
import json
from pathlib import Path
import struct
import urllib.request

KIT = Path(__file__).resolve().parents[1]
CSS_REV = "b1d7a907371bbe523d6f64e3af97f714fdbd6d6a"
ICON_REV = "e89583c9a0fbc5022d099fbe6f12132a756027a8"
CSS_REPO = "https://github.com/jdan/98.css"
ICON_REPO = "https://github.com/grassmunk/Chicago95"


def sources():
    entries = []
    for upstream, local in [
        ("LICENSE", "LICENSE"),
        ("README.md", "UPSTREAM-README.md"),
        ("style.css", "style.css"),
        ("fonts/src/ms-sans-serif/license.txt", "font-regular-license.txt"),
        ("fonts/src/ms-sans-serif-bold/license.txt", "font-bold-license.txt"),
    ]:
        entries.append(dict(
            path="resources/98-css/" + local,
            url=f"https://raw.githubusercontent.com/jdan/98.css/{CSS_REV}/{upstream}",
            source_page=f"{CSS_REPO}/blob/{CSS_REV}/{upstream}",
            category="component-source", expected_type="text",
            upstream_revision=CSS_REV,
            use_status="reference-only-uninstalled",
            provenance="CSS code: upstream MIT notice. Font notices: separate CC BY-SA 3.0 reconstruction; no font binaries collected.",
        ))
    entries.append(dict(
        path="resources/chicago95/UPSTREAM-README.md",
        url=f"https://raw.githubusercontent.com/grassmunk/Chicago95/{ICON_REV}/README.md",
        source_page=f"{ICON_REPO}/blob/{ICON_REV}/README.md",
        category="provenance-note", expected_type="text",
        upstream_revision=ICON_REV, use_status="reference-only-provenance-pending",
        provenance="README declares GPL-3.0+/MIT at repository level; this is not an asset-specific clearance.",
    ))
    icon_paths = [
        "actions/16/document-save.png", "actions/16/go-previous.png",
        "actions/16/view-grid.png", "actions/32/document-save.png",
        "actions/32/go-previous.png", "actions/32/system-search.png",
        "apps/16/accessories-text-editor.png", "apps/16/internet-mail.png",
        "apps/32/help-browser.png", "apps/32/internet-mail.png",
        "mimes/16/application-pdf.png", "mimes/32/text-x-generic.png",
        "mimes/32/x-office-document.png", "places/16/folder-documents.png",
        "places/16/folder-pictures.png", "places/32/folder-documents.png",
        "places/32/folder-pictures.png", "places/32/folder.png",
    ]
    for icon in icon_paths:
        upstream = "Icons/Chicago95/" + icon
        entries.append(dict(
            path="resources/chicago95/icons/" + icon,
            url=f"https://raw.githubusercontent.com/grassmunk/Chicago95/{ICON_REV}/{upstream}",
            source_page=f"{ICON_REPO}/blob/{ICON_REV}/{upstream}",
            category="pixel-icon-candidate", expected_type="png",
            upstream_revision=ICON_REV, use_status="reference-only-provenance-pending",
            provenance="Asset-specific origin/license not established. Do not copy into runtime assets without review; original replacements are preferred.",
        ))
    for era in ("win95", "win98", "win2000pro"):
        for kind, upstream in [
            ("desktop", "desktop/full"),
            ("file-manager", "system/managers/filemanager"),
        ]:
            entries.append(dict(
                path=f"resources/historical/{era}-{kind}.png",
                url=f"https://guidebookgallery.org/pics/gui/{upstream}/{era}.png",
                source_page=f"https://guidebookgallery.org/screenshots/{era}/",
                category="historical-screenshot", expected_type="png",
                upstream_revision=None, use_status="reference-only-not-for-production",
                provenance="Archived Microsoft UI screenshot curated by Marcin Wichary / GUIdebook; no production redistribution permission established.",
            ))
    return entries


def inspect(data, expected_type):
    details = dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    if expected_type == "png":
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or len(data) < 24:
            raise ValueError("Not a PNG (possibly a symlink placeholder or error response)")
        details["width"], details["height"] = struct.unpack(">II", data[16:24])
    else:
        data.decode("utf-8")
        if data.lstrip().lower().startswith((b"<!doctype html", b"<html")):
            raise ValueError("Unexpected HTML instead of source text")
    return details


def gather(entry):
    request = urllib.request.Request(entry["url"], headers={
        "User-Agent": "AcademicHomepage-DesignReferenceGatherer/1.0",
    })
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    details = inspect(data, entry["expected_type"])
    target = KIT / entry["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != data:
        raise ValueError(f"Refusing to overwrite changed resource: {target}")
    if not target.exists():
        target.write_bytes(data)
    return dict(entry, **details)


def verify():
    manifest = json.loads((KIT / "resources/manifest.json").read_text())
    for entry in manifest["resources"]:
        actual = inspect((KIT / entry["path"]).read_bytes(), entry["expected_type"])
        for key, value in actual.items():
            if entry[key] != value:
                raise ValueError(f"Mismatch: {entry['path']} ({key})")
    print(f"Verified {len(manifest['resources'])} resources: checksums, types, and PNG dimensions.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Offline validation only")
    args = parser.parse_args()
    if args.verify:
        verify()
        return
    with ThreadPoolExecutor(max_workers=5) as pool:
        resources = list(pool.map(gather, sources()))
    manifest = dict(
        schema_version=1, collected_on=date.today().isoformat(),
        purpose="Planning only; no resources are connected to Jekyll or approved for deployment.",
        revisions={"98.css": CSS_REV, "Chicago95": ICON_REV},
        resources=resources,
    )
    target = KIT / "resources/manifest.json"
    if target.exists():
        previous = json.loads(target.read_text())
        if previous["resources"] != resources:
            raise ValueError("Refusing to overwrite a changed manifest")
    else:
        target.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Gathered {len(resources)} resources ({sum(r['bytes'] for r in resources):,} bytes).")
    verify()


if __name__ == "__main__":
    main()
