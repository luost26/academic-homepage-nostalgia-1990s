#!/usr/bin/env python3
"""Gather a small user-selected Windows 98 icon review set, not runtime assets."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import json
import sys

sys.dont_write_bytecode = True
from gather_resources import KIT, gather, inspect

SOURCE = "https://win98icons.alexmeub.com/"
# Exact PNG links observed on the viewer page; numeric suffixes are not sizes.
SELECTION = [
    ("directory_closed-4.png", "Section / publication collection"),
    ("directory_open_file_mydocs-4.png", "Publications / academic documents"),
    ("notepad_file-2.png", "Paper / CV document"),
    ("notepad-2.png", "Blog / research notes"),
    ("paint_file-4.png", "Showcase / research images"),
    ("mailbox_world-2.png", "Contact / academic profiles"),
    ("help_book_small-2.png", "About / education"),
    ("calendar-0.png", "News / dated announcements"),
]
MANIFEST = KIT / "resources/win98icons/manifest.json"


def verify():
    manifest = json.loads(MANIFEST.read_text())
    for entry in manifest["resources"]:
        actual = inspect((KIT / entry["path"]).read_bytes(), "png")
        for key, value in actual.items():
            if entry[key] != value:
                raise ValueError(f"Mismatch: {entry['path']} ({key})")
    print(f"Verified {len(manifest['resources'])} user-selected Windows 98 icon candidates.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify()
        return
    entries = [dict(
        path="resources/win98icons/icons/" + filename,
        url=SOURCE + "icons/png/" + filename,
        source_page=SOURCE,
        category="user-selected-windows-98-icon", expected_type="png",
        proposed_mapping=mapping,
        use_status="user-preferred-planning-candidate-not-connected-to-site",
        provenance="Collection hosted by Alex Meub. User explicitly nominated this source. No explicit icon reuse license found on viewer page; do not infer an open-source artwork license.",
    ) for filename, mapping in SELECTION]
    with ThreadPoolExecutor(max_workers=4) as pool:
        resources = list(pool.map(gather, entries))
    manifest = dict(schema_version=1, collected_on=date.today().isoformat(),
                    purpose="Planning only; user-preferred icon collection, unmodified PNGs, no Jekyll connection.",
                    resources=resources)
    if MANIFEST.exists():
        if json.loads(MANIFEST.read_text())["resources"] != resources:
            raise ValueError("Refusing to overwrite changed icon inventory")
    else:
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Gathered {len(resources)} icons ({sum(entry['bytes'] for entry in resources):,} bytes).")
    for entry in resources:
        print(f"{entry['path'].split('/')[-1]}: {entry['width']}x{entry['height']}")
    verify()


if __name__ == "__main__":
    main()
