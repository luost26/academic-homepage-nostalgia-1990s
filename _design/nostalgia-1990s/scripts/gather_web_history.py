#!/usr/bin/env python3
"""Collect dated web-layout references, separate from the Windows UI kit."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import json
from gather_resources import KIT, gather, inspect

EXAMPLES = [
    ("yahoo-1998", "https://www.webdesignmuseum.org/uploaded/timeline/yahoo/yahoo-1998.png", "https://www.webdesignmuseum.org/gallery/yahoo-in-1998", "https://web.archive.org/web/19980630072557/http://www.yahoo.com/"),
    ("larry-page-homepage-1998", "https://www.webdesignmuseum.org/uploaded/fullscreen/larry-page-homepage-1998.png", "https://www.webdesignmuseum.org/gallery/larry-page-homepage-in-1998", "https://web.archive.org/web/19981202114029/http://www-pcd.stanford.edu/~page/"),
    ("sergey-brin-homepage-1998", "https://www.webdesignmuseum.org/uploaded/fullscreen/sergey-brin-homepage-1998.png", "https://www.webdesignmuseum.org/gallery/sergey-brin-homepage-in-1998", "https://web.archive.org/web/19980418143602/http://www-db.stanford.edu/~sergey/"),
    ("google-1998", "https://www.webdesignmuseum.org/uploaded/timeline/google/google-1998.png", "https://www.webdesignmuseum.org/gallery/google-1998", "https://web.archive.org/web/19981202230410/http://www.google.com"),
]


def verify():
    manifest = json.loads((KIT / "resources/web-history/manifest.json").read_text())
    for entry in manifest["resources"]:
        actual = inspect((KIT / entry["path"]).read_bytes(), "png")
        for key, value in actual.items():
            assert entry[key] == value, f"Mismatch: {entry['path']} ({key})"
    print(f"Verified {len(manifest['resources'])} web-history screenshots.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify()
        return
    entries = [dict(
        path=f"resources/web-history/{name}.png", url=url, source_page=museum,
        original_archive=archive, category="historical-web-screenshot", expected_type="png",
        use_status="reference-only-not-for-production",
        provenance="1998 website artifact reproduced by Web Design Museum; screenshots remain copyrighted by their respective owners. Research only.",
    ) for name, url, museum, archive in EXAMPLES]
    with ThreadPoolExecutor(max_workers=4) as pool:
        resources = list(pool.map(gather, entries))
    target = KIT / "resources/web-history/manifest.json"
    manifest = dict(schema_version=1, collected_on=date.today().isoformat(), resources=resources)
    if target.exists():
        assert json.loads(target.read_text())["resources"] == resources, "Refusing changed inventory"
    else:
        target.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Gathered {len(resources)} web references ({sum(r['bytes'] for r in resources):,} bytes).")
    verify()


if __name__ == "__main__":
    main()
