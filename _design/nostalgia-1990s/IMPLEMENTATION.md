# 1998 academic desktop companion — implementation

Implemented locally on 2026-09-13 following the user's approval. The user then
approved the finished design and requested screenshots, an Aero-format README,
and a commit/push to the nostalgia repository. No manual deployment or repository
settings changes are part of this handoff.

## Delivered

- A single shared 1280px-maximum silver frame for the homepage, publications,
  blog archive, every blog article, showcase, and 404/prompt layout.
- Navy-to-blue identity masthead; attached real navigation tabs; normal-flow
  header and document scrolling. No minimize/maximize/close buttons, fake menus,
  taskbar, address bar, boot screen, or simulated system state.
- Self-hosted, unmodified regular/bold pixel-grid MS Sans Serif reconstructions
  by lou. Native 11px chrome, metadata, buttons, and reading text; integer-grid
  headings retain their larger hierarchy. Body/button/code text sizes share
  one CSS variable so the reading text stays consistent with the controls.
  Math and code retain suitable readable faces. Attribution, license notices,
  and checksum inventories accompany the fonts.
- User-selected Windows 98 PNGs from Alex Meub's collection, unmodified on
  native 32x32 and 16x16 canvases. All section-heading icons use genuine 32x32
  variants; About me uses the tree icon. Contact buttons retain genuine 16x16
  PNG variants. Both sizes come from the collection's official ZIP, displayed
  one-to-one. The eight original 48x48 source assets are retained but not rendered.
  No downscaling or conversion is used. Source
  attribution and provenance accompany the assets; no
  unspecified open-source artwork license is claimed.
- Footer artwork/font attribution is collapsed by default behind an accessible
  "Artwork credits" disclosure, matching the Aero variant's behavior. The
  academic-homepage template link is text-only, as requested.
- Inset profile/portrait rail, left-aligned beveled contact/profile/CV links
  with classic icons beside their 11px labels. Email uses only a single-line
  address, with no "Email" prefix; contact links do not use the help-book icon.
  The homepage has one white document surface containing the existing
  biography and widgets.
- Document-style publication and blog archives with real year anchors and
  current-location states. Publication covers, metadata, abstracts, authors,
  links, and Semantic Scholar citation behavior are retained. Real cover images
  and generated bubble covers share the same recessed, dark-top/left and
  light-bottom/right beveled frame; original image files and proportions are
  retained. Missing covers
  use a redesigned title-seeded bubble visual hash: six opaque, dithered,
  stair-stepped bubbles in a limited classic palette, within a silver inset
  thumbnail. The original MD5 seed implementation/credits are retained in
  bubble_visual_hash.js. Pixels are batched into a few dozen SVG paths;
  no animation, randomness, external requests, or bitmap-cover filters are used.
  The graphic is decorative, and a quiet grid remains when JavaScript is off.
  Publication-entry link buttons use compact 24px minimum heights and 2px/8px
  padding, retaining the shared 11px text and larger 44px coarse-pointer targets.
  Contact, navigation, and other buttons retain their existing sizing.
- Blog articles share the outer frame and have accessible contents links,
  a mobile disclosure, KaTeX, Prism highlighting, and contained wide tables/code.
- Showcase groups/images retained; desktop Masonry, immediate normal-flow
  stacking on mobile, and classic manual carousel controls with pressed-state
  announcements. Layout recalculates after fonts, images, and slide changes.
- Layout 2 removed from source, navigation, and generated output.
- Keyboard skip link, visible dotted focus, stable scrollbar alignment, minimal
  motion, reduced-motion-aware lazy-image effects, and a clean print stylesheet.
- Original CDN integrity attributes retained; research/tool directories
  explicitly excluded from Jekyll output. No wholesale 98.css import.

## Verification evidence

Both configured-subpath and site-root Jekyll builds passed. The offline checker
verified eight generated pages, 175 local resource/anchor references, four papers,
three posts, fourteen showcase items, six news entries, and twenty-two unchanged
icon/font files. It also verifies original content/image files remain unchanged,
consistent navigation URLs, unique IDs, shared landmarks, attribution files,
native icon dimensions, and exclusion of research/tool output. Heading/contact
checks also read each source PNG's intrinsic dimensions to reject larger artwork
even when its HTML dimensions are set to 32 or 16. About me must use the tree icon.
Footer checks require a closed credits disclosure and no icon markup on every
generated page. The display configuration is preserved except for the requested
removal of the template-link icon.
Cover checks require one seeded, decorative pixel canvas for every publication
without a cover. Node tests verify deterministic patterns, bounded 2px geometry,
opaque classic colors, safe input handling, batched paths, and idempotent rendering.

The two unchanged sample-blog `../blob/master/LICENSE` links are already broken
in the baseline. The checker reports exact, git-HEAD-verified exceptions rather
than silently treating them as valid links. No Markdown content was rewritten
to invent a new destination.

Browser checks covered all page types at 320px and 768px; additional 375px
article/archive checks and 1440px desktop checks passed without horizontal
overflow. The shared frame measured 1280px on desktop; scrollbar reservation
keeps short and long pages aligned. Bitmap glyphs, native icons, portrait,
publication covers, and institution logos were visually reviewed.

Final homepage and publications screenshots are saved as unmodified browser
captures in assets/images/screenshots/homepage.jpg and publications.jpg
(1265x712 each). These use the normal desktop viewport; a stitched full-page
capture was rejected because it duplicated page content. The README follows
the Aero variant's introduction, badges, screenshots, theme, credits, and setup
section structure.

Runtime checks confirmed native publication-year and article-heading anchors,
current states, mobile/desktop contents disclosure, 317 highlighted code tokens
in the sample article, rendered homepage/showcase math, and functional carousel
Next/slide-selection controls. Keyboard Tab focused the skip link; Enter moved
focus to main content with a dotted focus ring. Code/selection/metadata/badge
colors use dark classic palette pairs. Print and reduced-motion rules were
reviewed in source; a physical print/PDF export was not performed.

Semantic Scholar remains an optional external service: actual citation badges
rendered during checks; transient network failures were also observed and are
handled by the existing citation script. No publication content depends on a
successful API response.

## Reproduce

From the nostalgia repository, with its installed Ruby/Bundler environment:

```sh
bundle exec jekyll build --trace
python3 scripts/verify_classic.py _site
node scripts/test_visual_hash.js
bundle exec jekyll serve --host 127.0.0.1 --port 4188
```

For site-root compatibility, build to a fresh temporary directory with
`--baseurl '' --destination <directory>`, then run
`python3 scripts/verify_classic.py <directory> --baseurl ''`.

On this host, the default shell resolves system Ruby 2.6 while installed gems
belong to Ruby 3.1.3. Verification used the existing binary
`/Users/luost/.rubies/ruby-3.1.3/bin/ruby` to invoke the existing Bundler executable.
No gems, system fonts, or global settings were installed or changed.

The local preview is at
[academic-homepage-nostalgia-1990s](http://127.0.0.1:4188/academic-homepage-nostalgia-1990s/).
