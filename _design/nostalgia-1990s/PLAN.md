# 1998 academic desktop companion — design plan

Status: implemented locally after explicit user approval, 2026-09-13.
See [implementation and verification notes](IMPLEMENTATION.md). The specification
below records the approved direction and its original planning gates; statements
about deferred implementation are historical, not current repository status.

Confirmed refinements, 2026-09-13: no minimize/maximize/close controls; visibly low-resolution typography; no exact Windows clone; and no literal recreation of a rough early personal website. The latest direction integrates Windows 98 materials into a deliberately composed academic website. Homepage code remains unchanged.

User-selected icon source: [Alex Meub's Windows 98 Icon Viewer](https://win98icons.alexmeub.com/) is now the preferred collection. Eight unmodified PNG candidates have been gathered and checksummed. This supersedes the proposal to prioritize original replacement artwork; the older Chicago95 kit remains a historical comparison. The existing conversation composition still uses its earlier review icons, not the newly selected collection.

## Recommended direction

An **academic desktop companion circa 1998**: a modern, readable academic page with a coordinated Windows 98 material system. A restrained teal surround, silver raised frame, navy/blue masthead, attached navigation tabs, inset profile area, and white document surface establish the era together. Chunky bitmap typography and a small coherent pixel-icon family reinforce the same visual language.

Think of an academic knowledge base or desktop companion, not a desktop simulator and not an untouched GeoCities page. This is an evocative synthesis, not a claim that academic sites universally looked this way in 1998. Period websites supply direct, link-rich content; Windows 98 supplies the stronger visual identity across the whole composition, not only isolated buttons. Do not invent CD-ROM packaging, boot behavior, a taskbar, or system commands to justify the metaphor.

No frosted glass, glow, rounded card grid, glossy icon shading, or photographic nature banner. Implementation starts only after an explicit request. The latest conversation mockup supersedes the three-OS material comparison as the composition reference; that earlier comparison remains useful for examining primitives.

## Context and repository baseline

Reviewed the referenced task **Plan Frutiger Aero redesign** (`01a09b7b-f1b0-7f62-9ae8-436b4429e78c`, local), including its subsequent user refinements.

Carry forward as proposed preferences:

- One homepage layout rather than Home Layout 2.
- A consistent maximum frame width across Home, Publications, Blog, Showcase, and error pages; use the Aero task's eventual 1280px ceiling as a starting point, not a fixed canvas.
- A header in normal document flow. No header-height tracking or sticky-header anchor offsets.
- Preserve the Jekyll content model, institution logos, portrait, publication images, Markdown, math, code, citations, and gallery behavior.
- Gather resources with provenance and review their appearance before implementation.

The nostalgia repo is a separate, clean baseline, not a copy of the finished Aero theme. At inspection it was on `main`, HEAD `b9dc1eb`, with origin `git@github.com:luost26/academic-homepage-nostalgia-1990s.git`. Its baseurl is already `/academic-homepage-nostalgia-1990s`.

It currently still has Home Layout 2, Bootstrap cards, rounded styles, different container classes, and a fixed navbar with body top padding. Those are future migration targets; none have been changed. The profile contains template placeholders, so do not invent a real researcher biography or publication record.

## Historical evidence and how to use it

Late-1990s web design had several overlapping strands, not one universal style. [Yahoo's June 1998 archive](https://web.archive.org/web/19980630072557/http://www.yahoo.com/) illustrates compact directories and blue category links; [Larry Page's December 1998 academic homepage](https://web.archive.org/web/19981202114029/http://www-pcd.stanford.edu/~page/) illustrates direct personal/academic information and images on a plain document. Personal web culture also used tiled backgrounds and small GIF ornaments, as documented by the [GeoCities Research Institute](https://blog.geocities.institute/archives/date/2014/06). These examples establish recognizable strands, not measured popularity rankings.

| Source layer | Borrow | Deliberately adapt or omit |
|---|---|---|
| Period academic web | Visible affiliation/contact, direct prose, linked paper lists | Deliberate hierarchy, stable alignment, responsive reading measure |
| Directory/portal web | Clear section index, compact labeled navigation, link-rich information | No cluttered portal dashboard or unrelated link directory |
| Personal web | Characterful color, subtle repeated texture, small pixel motifs | No blink, autoplay, random GIF collage, fake counters, or construction signs |
| Windows 98 | Consistent silver bevels, inset document surfaces, attached tabs, navy selection, pixel typography/icons | No literal OS shell, title-bar controls, fake menus, or desktop interaction |

The strongest OS anchor is [Windows 98's original interface](https://guidebookgallery.org/screenshots/win98/); [95](https://guidebookgallery.org/screenshots/win95/) and [2000](https://guidebookgallery.org/screenshots/win2000pro/) remain secondary palette/material references. Historical serif body text was common in the gathered web examples, but the requested stronger pixel character takes precedence in this variant.

Do not introduce XP Luna's rounded blue frames, green Start button, Bliss wallpaper, or Vista glass. Recognizability should come from a coordinated material system, not additional nostalgic props.

## Visual rules

### Proposed palette, not a pixel-perfect OS specification

| Role | Default proposal | Treatment |
|---|---|---|
| Page surround | `#008080` | Teal with an optional quiet, original dither; a margin, not an interactive desktop |
| Main chrome | `#C0C0C0` | Opaque silver-gray |
| Raised highlights | `#FFFFFF`, `#DFDFDF` | Two crisp top/left edges |
| Shadows/frame | `#808080`, `#0A0A0A` | Bottom/right bevels, no diffuse glow |
| Masthead/accent | `#000080` → `#1084D0` | Broad enough to anchor the composition; not a fake application title bar or glossy reflection |
| Reading pane | `#FFFFFF` | Inset border with generous inner padding |
| Main text | `#222222` | Solid, readable text |
| Text links | `#0000CC` | Underlined; visited state remains distinguishable |
| Selection | `#000080` with white text | Paired with position, text, or a pressed state |

Bevel and title-bar primitives can be studied in [98.css](https://jdan.github.io/98.css/). The kit holds its source as a reference, not an imported dependency.

### Shape, type, and density

- Rectangular corners, consistent 1–2px stepped edges, a single raised outer frame, attached tabs, and genuine inset regions. Use hierarchy rather than a separate window for every section. The masthead carries the researcher's identity, not an application caption.
- Typography must visibly evoke a low-resolution Windows desktop. Use the pixel-grid MS Sans Serif regular/bold reconstructions by lou as the review candidates, not smooth Tahoma/Arial. The revised materials use 11px native-grid chrome and 22px doubled-grid reading text. Prefer native/integer scales over arbitrary interpolation; keep real selectable text, not rasterized text images. Final body scale remains a readability review decision, with the bitmap character retained.
- These are reconstructions, not Microsoft's original font binaries. Their separate CC BY-SA 3.0 notices must remain with any redistributed font material; the CSS's MIT notice does not cover them. Two unmodified WOFF2 font candidates have now been gathered for the samples, with a supplementary checksum inventory. No system fonts have been installed and no font has been added to homepage layouts.
- Pixel texture now belongs in the typography as well as icons and chrome, per user feedback. Do not apply pixel filters to institution logos, scientific figures, or portraits. Math/code still need appropriate readable faces and complete glyph coverage.
- Use a small matched family from the user-selected Windows 98 collection, with visible labels. All eight downloaded PNGs have intrinsic 48x48 canvases; the numeric filename suffix is not a pixel size. Review these at native 48px as larger section motifs. Use text-first compact controls until actual 16/32px resources are verified; do not silently downsample the supplied 48px files. Keep source attribution and provenance recorded without assuming the artwork is open-source merely because it is downloadable.
- Leave room around controls. Period density is a visual cue, not a reason for tiny click targets.

## Shared shell and homepage composition

One centered, raised website frame, `max-width` provisionally 1280px, with fluid outer margins. Keep the inner reading measure narrower than that ceiling. On desktop, use a 250–285px identity/contact rail and a flexible academic document area. On smaller screens, switch to normal stacked flow. Silver framing should be visually substantial enough to establish the era, while white reading space remains dominant.

```text
Teal / subtly dithered page margin
└── Raised silver website frame
    ├── Researcher name + affiliation              [navy/blue masthead]
    ├── Home | Publications | Blog | Showcase       [attached real navigation]
    ├── Inset profile rail    │ White document surface
    │   portrait + name       │ About Me
    │   position/affiliation  │ Education / Experience / Awards
    │   Email / Scholar / CV  │ News
    │   other academic links  │ Selected Publications
    └── Updated date / template credit              [ordinary site footer]
```

The masthead and navigation scroll normally with the page. No fake File/Edit menu, address bar, breadcrumb filesystem path, connection indicator, or OS status bar. A thin beveled divider can organize the site footer without inventing system state.

Do not display minimize/maximize/close controls anywhere in the proposed frame, including decorative versions. This is a confirmed user preference, not an optional treatment. The main homepage should never require dragging, double-clicking, closing windows, using a Start menu, or dismissing a boot screen to reach its content.

### Component mappings

| Existing content | Proposed classic treatment |
|---|---|
| Profile | Inset identity/contact rail; retained portrait, clear position/affiliation, labeled beveled contact links |
| About Me | White document pane with clear heading; short accent rule rather than another heavy window frame |
| Education / experience / awards | Property-sheet-style grouped sections, existing logos retained; readable dates |
| News | Compact notice list with date column that wraps on narrow screens; no invented unread count |
| Selected publications | Document-list rows with normal covers, prominent title, authors, venue, abstract, and raised Paper/Code/Project links |
| Missing publication cover | Prefer a quiet, original document motif or no cover; assess the existing bubble hash rather than keeping an Aero-like decoration automatically |
| Footer | Quiet text and beveled separator with actual update information and existing credit; no simulated status fields |

Academic brand links should retain their names. A generic folder or document icon is decoration, not a replacement for Google Scholar, ORCID, GitHub, or PDF labels.

## Page-by-page extension

- **Publications:** A document list grouped by year within the shared inset reading surface. Year navigation uses real anchors styled as compact raised/pressed controls. Keep abstracts readable; do not force metadata into a narrow spreadsheet table. No file-manager commands or invented view toggle.
- **Blog archive:** The same document-list grammar and year links. Existing dates, tags, and excerpts remain data-driven.
- **Blog article:** An opaque document surface inside the shared frame, with a restrained help-document flavor rather than a replicated WordPad window. Narrow reading measure around 70–80 characters; contents rail becomes an in-flow disclosure on mobile. Keep math, citations, code, and wide tables intact.
- **Showcase:** Inset picture frames and simple captions, retaining the existing collection grouping and functional carousel. No retro image filter on research figures or photographs.
- **404 / prompt:** A compact classic message-box presentation with a useful Home link, not an obstructive browser alert. Preserve usable titles and focus semantics.
- **Home Layout 2:** Plan its removal from navigation and output, following the earlier user preference, but leave it untouched until implementation is requested.

## Responsive, accessible, and usable behavior

- The same nostalgic identity must survive at 320px without horizontal overflow. Stack profile/content and wrap navigation. The latest conversation specimen explores the integrated composition; it is not homepage implementation.
- No fixed-height desktop or internally scrolling main content. The page itself scrolls. No chrome covers content.
- Use real links/buttons, semantic headings and landmarks, visible current-page state, keyboard focus, and a skip link. Do not hijack browser shortcuts or add access-key conflicts to imitate menus.
- Fine-pointer controls may look compact; touch targets should be about 44px where practical. Body text and all essential labels remain legible at zoom.
- Test contrast on actual pane/selection backgrounds. Do not copy historically low-contrast disabled text for informative content.
- Prefer minimal motion. No boot animation, simulated loading delays, click sounds, or cursor trails by default. Respect reduced motion if transitions are introduced.
- Print as a clean document: no teal desktop, chunky chrome, or artificial window controls.

## Future implementation map — not executed

| Area | Likely files and considerations |
|---|---|
| Shared outer frame | `_layouts/default.html`, `_includes/navbar.html`, `_includes/footer.html`; normal-flow header and one width policy |
| Separate layouts | `_layouts/blog_post.html`, `_layouts/prompt.html`; avoid duplicated theme logic |
| Reusable primitives | Future `_includes/classic/` and a namespaced stylesheet; identity masthead, bevels, attached navigation, inset pane, labeled icon/link |
| Academic widgets | `_includes/widgets/profile_card_mini.html`, `profile_card_bio_only.html`, `experience_card.html`, `news_card.html`, `publication_card.html`, `publication_item.html`, `blog_card.html` |
| Page entry points | `index.html`, `publications.html`, `blog.html`, `showcase.html`, `404.html`, `_data/navigation.yml`; proposed Layout 2 cleanup |
| Existing styles/behavior | `assets/css/global.css`, `assets/css/blog.css`, `assets/js/blog.js`, `assets/js/bubble_visual_hash.js`; examine navbar padding, rounding, anchor assumptions, and fallback imagery |
| Content | Keep `_data/*.yml` and Markdown collections unchanged unless a content change is explicitly requested |
| Deploy paths | Preserve the already correct nostalgia baseurl and use `relative_url` for local resources |

Do not import all of 98.css globally over Bootstrap: its element selectors, root variables, and typography can affect articles and existing widgets. Prefer narrowly scoped, attributed primitives or a carefully scoped subset once the implementation approach is approved. Do not copy the Aero implementation's entire dependency/layout changes just to inherit its preferences.

The kit is under `_design/`, separate from `assets/` and disconnected from the layouts. Jekyll normally omits unconfigured underscore directories; verify that behavior during the future build and keep historical/provenance-pending resources out of published output.

## Review gates and later milestones

1. **Current milestone: direction and resources.** Review this plan, [resource catalogue](RESOURCES.md), and the integrated 1998 desktop-companion mockup. Prior OS samples are primitive references only. All homepage code stays unchanged.
2. **After explicit implementation request: one homepage preview.** Build the shared frame, profile, About Me, and one publication row. Review strength of period identity, reading comfort, chrome density, and text sizing before touching every page.
3. **Extend the approved system.** Apply to archives, blog article, gallery, and error/prompt pages, keeping content and behavior intact. Select the final small icon family from the user-preferred collection, preserve attribution, and review reuse terms/provenance before public redistribution. Original art is a fallback for gaps, not the preferred starting point.
4. **Verify before publishing.** Jekyll build at configured subpath and site root; local-link and missing-image checks; desktop/tablet/320px/375px layouts; zoom, keyboard, contrast, print, native anchors, menus, citations, math, code, and carousels. Confirm no `_design/` research files entered `_site`.

No commit, push, deployment, dependency installation, config edit, or homepage implementation is included in this planning milestone.

## Remaining choices (non-blocking)

- Review a restrained teal surround versus a subtle dither, and solid navy versus a navy/blue masthead. These are material variations within one design, not separate OS replicas.
- Alex Meub's Windows 98 collection is the user-preferred icon source. Settle the exact motifs and display sizes during the next composition review; retain its source attribution. No explicit icon reuse license was found on the viewer page, so do not label the artwork MIT or otherwise production-cleared without further evidence.
- No Start menu is proposed. Site navigation and academic contact links already provide the useful destinations.

These choices can be made at review; no further work is needed to implement them now.
