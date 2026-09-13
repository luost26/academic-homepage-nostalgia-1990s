#!/usr/bin/env python3
"""Verify resources and mechanically embed fonts and optional review icons."""

import argparse
import base64
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fragment", type=Path, nargs="?")
    parser.add_argument("--review-icons", action="store_true", help="Embed research-only icon candidates in an isolated sample")
    args = parser.parse_args()
    font_root = Path(__file__).resolve().parents[1] / "resources/98-css/fonts"
    manifest = json.loads((font_root / "manifest.json").read_text())
    replacements = {}
    for entry, marker in zip(manifest["resources"], ("PLACEHOLDER_REGULAR", "PLACEHOLDER_BOLD")):
        data = (font_root / entry["path"]).read_bytes()
        assert data[:4] == b"wOF2", "Unexpected font type"
        assert len(data) == entry["bytes"], "Font size mismatch"
        assert hashlib.sha256(data).hexdigest() == entry["sha256"], "Font checksum mismatch"
        replacements[marker] = base64.b64encode(data).decode("ascii")
    if args.review_icons:
        kit = font_root.parents[2]
        inventory = json.loads((kit / "resources/manifest.json").read_text())
        entries = {entry["path"]: entry for entry in inventory["resources"]}
        icons = {
            "PLACEHOLDER_FOLDER": "resources/chicago95/icons/places/32/folder-documents.png",
            "PLACEHOLDER_DOCUMENT": "resources/chicago95/icons/mimes/32/text-x-generic.png",
            "PLACEHOLDER_MAIL": "resources/chicago95/icons/apps/16/internet-mail.png",
        }
        for marker, relative in icons.items():
            entry = entries[relative]
            data = (kit / relative).read_bytes()
            assert data[:8] == b"\x89PNG\r\n\x1a\n", "Unexpected icon type"
            assert len(data) == entry["bytes"], "Icon size mismatch"
            assert hashlib.sha256(data).hexdigest() == entry["sha256"], "Icon checksum mismatch"
            replacements[marker] = base64.b64encode(data).decode("ascii")
    if args.fragment:
        source = args.fragment.read_text()
        for marker, encoded in replacements.items():
            source = source.replace(marker, encoded)
        args.fragment.write_text(source)
        print(f"Embedded {len(replacements)} verified, unmodified resources in the planning sample.")
    else:
        print("Verified two WOFF2 fonts: type, byte size, and SHA-256.")


if __name__ == "__main__":
    main()
