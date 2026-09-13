# Windows Classic visual resource catalogue

Implementation update: the two fonts and eight user-selected icons have now
been copied, unmodified, into isolated homepage asset folders after approval.
Attribution and checksum inventories accompany those files. Historical images
and earlier Chicago95 candidates remain excluded research material. The catalogue
below records collection-time status; see [implementation notes](IMPLEMENTATION.md).

Collected 2026-09-13. This is an offline research kit, not an installed theme or production-cleared asset bundle. The original 30 resources total 177,557 bytes. Two WOFF2 fonts add 12,772 bytes, four historical web screenshots add 280,290 bytes, and eight user-selected Windows 98 icons add 4,713 bytes. Total downloaded material: 475,332 bytes (about 464 KiB), excluding documentation, inventories, and scripts.

## What is here

| Material | Count | Local location | Intended use |
|---|---:|---|---|
| Historical desktop and file-manager screenshots | 6 PNGs | `resources/historical/` | Study coordinated Windows materials; not instructions to replicate OS navigation |
| Historical academic/directory/search web screenshots | 4 PNGs | `resources/web-history/` | Compare period web content and composition; reference-only |
| Alex Meub Windows 98 icon candidates | 8 PNGs, all intrinsic 48x48 | `resources/win98icons/icons/` | User-preferred source; small academic-site selection, unmodified |
| Earlier Chicago95 pixel-icon candidates | 18 PNGs: 8 at 16px, 10 at 32px | `resources/chicago95/icons/` | Historical comparison; superseded as preferred collection, provenance pending |
| Pinned 98.css stylesheet | 1 CSS file | `resources/98-css/style.css` | Study title bars, bevels, controls, inset panes, and status fields; uninstalled |
| Upstream README and licensing/provenance notes | 5 text files | `resources/98-css/`, `resources/chicago95/` | Keep code/font terms and source context visible |
| Bitmap-style MS Sans Serif reconstructions, regular and bold | 2 WOFF2 files | `resources/98-css/fonts/` | User-requested low-resolution typography in the isolated planning samples; not system-installed |
| Per-file source/checksum inventory | 1 JSON manifest | `resources/manifest.json` | Trace URLs, pinned revisions, byte sizes, image dimensions, and use status |
| Supplementary font inventory | 1 JSON manifest | `resources/98-css/fonts/manifest.json` | Font source, separate license, checksum, and sample-only status |
| Supplementary web-history inventory | 1 JSON manifest | `resources/web-history/manifest.json` | Screenshot source, archived date/URL, dimensions, checksum, and research-only status |
| User-selected icon inventory | 1 JSON manifest | `resources/win98icons/manifest.json` | Exact PNG URL, intended academic mapping, dimensions, checksum, and source notes |

Total: 44 downloaded resources (30 baseline + 2 fonts + 4 web references + 8 selected icons), plus inventories. The earlier Chicago95 selection is not a matched two-size set. The newly selected collection supplies 48x48 canvases for all eight downloaded files.

## Preferred icon collection — user selected

[Windows 98 Icon Viewer by Alex Meub](https://win98icons.alexmeub.com/) is the preferred source following the user's explicit suggestion. These exact individual PNG links were observed in the viewer; no complete archive, executable, or unrelated collection was downloaded.

| Candidate | Proposed use |
|---|---|
| [directory_closed-4.png](resources/win98icons/icons/directory_closed-4.png) | Section / publication collection |
| [directory_open_file_mydocs-4.png](resources/win98icons/icons/directory_open_file_mydocs-4.png) | Publications / academic documents |
| [notepad_file-2.png](resources/win98icons/icons/notepad_file-2.png) | Paper / CV document |
| [notepad-2.png](resources/win98icons/icons/notepad-2.png) | Blog / research notes |
| [paint_file-4.png](resources/win98icons/icons/paint_file-4.png) | Showcase / research images |
| [mailbox_world-2.png](resources/win98icons/icons/mailbox_world-2.png) | Contact / academic profiles |
| [help_book_small-2.png](resources/win98icons/icons/help_book_small-2.png) | About / education |
| [calendar-0.png](resources/win98icons/icons/calendar-0.png) | News / dated announcements |

Every downloaded PNG has an intrinsic 48x48 canvas; suffixes such as `-2` or `-4` do not identify its size. Review the supplied files at native size with pixel-preserving rendering. Do not infer 16/32px availability, or downsample them for compact controls without a visual review. Folder/documents, document, paint-file, and mailbox images were inspected locally, and the collection was inspected in the browser.

Record attribution to Alex Meub's collection and retain the exact source URLs. No explicit icon reuse license was found on the viewer page; the user's source selection is not evidence of an MIT/open-source artwork license. The files remain planning candidates disconnected from Jekyll. The current conversation mockup still shows the earlier Chicago95 review assets; replace those in the next requested composition revision.

## Period web references and the latest synthesis

The user does not want a literal, rough late-1990s website. These references help separate period web content conventions from Windows 98's stronger material identity. The recommended synthesis is a composed academic desktop companion: silver relief, navy/blue identity masthead, attached navigation, inset regions, white reading space, and bitmap typography throughout a normal responsive website.

| Example | Screenshot / source | Archived original | Use in review |
|---|---|---|---|
| Yahoo, June 1998 | [Local screenshot](resources/web-history/yahoo-1998.png), [museum page](https://www.webdesignmuseum.org/gallery/yahoo-in-1998) | [June 30, 1998](https://web.archive.org/web/19980630072557/http://www.yahoo.com/) | Compact directories and link-rich organization, not an OS shell |
| Larry Page's academic homepage, December 1998 | [Local screenshot](resources/web-history/larry-page-homepage-1998.png), [museum page](https://www.webdesignmuseum.org/gallery/larry-page-homepage-in-1998) | [December 2, 1998](https://web.archive.org/web/19981202114029/http://www-pcd.stanford.edu/~page/) | Direct identity, contact and academic information; adapt the loose composition |
| Sergey Brin's academic homepage, April 1998 | [Local screenshot](resources/web-history/sergey-brin-homepage-1998.png), [museum page](https://www.webdesignmuseum.org/gallery/sergey-brin-homepage-in-1998) | [April 18, 1998](https://web.archive.org/web/19980418143602/http://www-db.stanford.edu/~sergey/) | Additional academic/personal page reference |
| Google, December 1998 | [Local screenshot](resources/web-history/google-1998.png), [museum page](https://www.webdesignmuseum.org/gallery/google-1998) | [December 2, 1998](https://web.archive.org/web/19981202230410/http://www.google.com) | Plain functional controls and flat section organization |

The museum supplies the downloaded PNGs; its cited Wayback captures identify the original sites/dates. Original Yahoo and Larry Page HTML were also retrieved during research. The Sergey archive could not be fetched in that session; its screenshot/date attribution relies on the museum. These are curated examples, not quantitative evidence for a single most popular style. All four images are research-only, not licensed homepage decoration. Their recorded sources and checksums prevent a silent refresh.

## Historical visual references

These are screenshots of the original Microsoft interfaces archived by Marcin Wichary's GUIdebook, not licensed website backgrounds. Store them as research material only; no production redistribution permission has been established.

| Era | Gallery/source | Downloaded samples | What to study |
|---|---|---|---|
| Windows 95 | [GUIdebook: Windows 95](https://guidebookgallery.org/screenshots/win95/) | [Desktop](resources/historical/win95-desktop.png), [My Computer](resources/historical/win95-file-manager.png) | Solid title bar; crisp bevels; white icon pane; segmented status strip |
| Windows 98 | [GUIdebook: Windows 98](https://guidebookgallery.org/screenshots/win98/) | [Desktop](resources/historical/win98-desktop.png), [My Computer](resources/historical/win98-file-manager.png) | Gradient title bar; layered toolbar; left context pane beside a white main pane |
| Windows 2000 Professional | [GUIdebook: Windows 2000 Pro](https://guidebookgallery.org/screenshots/win2000pro/) | [Desktop](resources/historical/win2000pro-desktop.png), [My Computer](resources/historical/win2000pro-file-manager.png) | Warmer gray chrome; subdued title gradient; compact controls; readable document surfaces |

The original image URLs and dimensions are in the manifest. Study the consistency between frame, controls, selection, typography, and inset regions. Borrow that material relationship without reproducing title-bar controls, menus, an address bar, taskbar, or status fields. Screenshots are not live UI assets.

## Component reference: 98.css

- [Official documentation and live component examples](https://jdan.github.io/98.css/)
- [Pinned repository revision](https://github.com/jdan/98.css/tree/b1d7a907371bbe523d6f64e3af97f714fdbd6d6a)
- [Upstream CSS code license](https://github.com/jdan/98.css/blob/b1d7a907371bbe523d6f64e3af97f714fdbd6d6a/LICENSE), retained locally as `resources/98-css/LICENSE`.

The stylesheet and code notice are collected for inspection only. Nothing imports them. The code notice is MIT; retain it when copying substantial code. Any future adoption needs a scoped integration review because the stylesheet has global element/root rules.

Fonts are a separate concern. The upstream regular and bold MS Sans Serif reconstructions by **lou** carry CC BY-SA 3.0 notices, copied into `font-regular-license.txt` and `font-bold-license.txt`. After the user found the original smooth typography insufficiently nostalgic, two unmodified WOFF2 reconstructions were downloaded and embedded in the isolated material samples, alongside attribution. This supersedes the initial Tahoma/Arial proposal. Use native 11px or doubled 22px grid sizing for review rather than scaling the pixel glyphs to arbitrary intermediate sizes. No Microsoft-original font files or system-installed fonts are involved.

## Earlier icon vocabulary: Chicago95 candidates

- [Chicago95 project](https://github.com/grassmunk/Chicago95)
- [Pinned icon source tree](https://github.com/grassmunk/Chicago95/tree/e89583c9a0fbc5022d099fbe6f12132a756027a8/Icons/Chicago95)
- [Pinned README/provenance note](resources/chicago95/UPSTREAM-README.md)

The README lists GPL-3.0+/MIT at repository level. An asset-specific origin/license for each selected image was not established. That declaration alone is not treated as permission to redistribute individual Windows-like icons. **Every downloaded icon is marked `reference-only-provenance-pending`.** Do not move them into `assets/` or deploy them without additional review. The separate Puffy mascot license is not applied to the standard Chicago95 icons.

| Motif | Selected sizes | Possible academic mapping |
|---|---|---|
| Document folder | 16, 32 | Publications / year collections |
| Picture folder | 16, 32 | Showcase |
| Generic folder | 32 | Broad section/home navigation cue |
| Mail | 16, 32 | Email/contact |
| Text editor | 16 | Blog/notes |
| PDF document | 16 | Paper/PDF link |
| Generic text document | 32 | CV/document motif |
| Office document | 32 | Publication/document motif |
| Floppy/save | 16, 32 | Download cue only; never imply saving site state |
| Back arrow | 16, 32 | Back to archive/section |
| Grid/view | 16 | Gallery/list display vocabulary; does not authorize a new toggle |
| Search | 32 | Vocabulary only; do not show unless real search exists |
| Help/book | 32 | Education/about/help vocabulary |

The generic mappings are proposed design semantics, not the meanings of existing homepage data fields. Use visible labels. Retain research covers, institution logos, and portraits without pixel filters.

All selected files are actual PNGs, not Git symlink text. Their native dimensions were checked. Alex Meub's Windows 98 collection is now preferred; original artwork is only a fallback for gaps or unresolved provenance. Avoid importing glossy Oxygen/Vista icons from the sibling variant.

Visual review also found application-specific marks in the PDF and office-document candidates, and stylistic variation between some 16px/32px motifs. These are vocabulary references, not a cohesive approved production set. Prefer generic original document art over Adobe/Word-like marks in the final navigation.

The integrated desktop-companion conversation sample uses only the generic folder, text-document, and mail candidates, embedded unmodified at native dimensions for research review. Its attribution identifies them as research-only with production provenance pending. `embed_sample_fonts.py <fragment> --review-icons` verifies those three against the baseline inventory before mechanical embedding; it does not place anything in homepage assets.

## Resource gaps intentionally left open

- No Microsoft logos, OS wallpaper binaries, sound pack, animated boot screen, retro cursor bundle, or full desktop simulator is needed.
- The website margin can be a solid teal CSS color or subtle original dither. It is not an interactive desktop and needs no downloaded wallpaper.
- No raster/generated artwork is needed for beveled buttons or title strips; CSS is a better fit for those primitives.
- The user has selected the preferred icon source; exact production motifs/sizes remain to be reviewed. Keep attribution and reuse provenance recorded, without claiming an unspecified artwork license is cleared.

## Reproduce and validate

From the nostalgia repository root:

```sh
python3 _design/nostalgia-1990s/scripts/gather_resources.py --verify
python3 _design/nostalgia-1990s/scripts/embed_sample_fonts.py
python3 _design/nostalgia-1990s/scripts/gather_web_history.py --verify
python3 _design/nostalgia-1990s/scripts/gather_win98icons.py --verify
```

All four checks are offline. They validate the original 30 files, two fonts, four web references, and eight user-selected icons respectively, using recorded sizes/checksums and PNG dimensions or WOFF2 signatures. Running a gather script without `--verify` fetches its recorded URLs and refuses to overwrite modified files or inventories. Font URLs are recorded separately. Historical archive URLs are not content-addressed; changes require explicit review, not a silent refresh. PNG header validation is not a full image decoder; the historical OS screenshots and earlier selected icons were also visually inspected. The Larry Page web screenshot was inspected locally; the Yahoo and Google pages were inspected in the research browser.

No downloaded code or installers were executed. No dependency or system font was installed, and no stylesheet, font, icon, or screenshot was connected to Jekyll. The font supplement is used only in the revised planning samples. Keep this underscore-prefixed research folder out of future build output and verify that during implementation. Do not commit/push this kit until asked, especially while its icon provenance remains unresolved.
