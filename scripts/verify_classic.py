#!/usr/bin/env python3
"""Offline integrity/link/content checks for a built classic homepage variant."""

import argparse
from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import subprocess
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
# These two unchanged Markdown demonstration links are already broken in HEAD.
BASELINE_EXAMPLES = {'2024/01/01/blog-post-1.html', '2025/01/01/blog-post-2.html'}


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = Counter()
        self.classes = Counter()
        self.tags = Counter()
        self.references = []
        self.navigation = []
        self.in_nav = False
        self.images = []
        self.visual_hashes = []
        self.credit_details = []
        self.footer_icons = []
        self.in_footer = False
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags[tag] += 1
        classes = attrs.get('class', '').split()
        self.classes.update(classes)
        if tag == 'footer':
            self.in_footer = True
        if tag == 'details' and 'classic-credits' in classes:
            self.credit_details.append(attrs)
        if self.in_footer and tag == 'i':
            self.footer_icons.append(attrs)
        if attrs.get('id'):
            self.ids[attrs['id']] += 1
        for key in ('href', 'src', 'data-src'):
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'svg' and 'bubble-visual-hash' in classes:
            self.visual_hashes.append(attrs)
        if tag == 'nav' and 'classic-navigation' in classes:
            self.in_nav = True
        if self.in_nav and tag == 'a':
            self.navigation.append(attrs)

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False
        if tag == 'footer':
            self.in_footer = False


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def asset_integrity(root):
    checked = 0
    icon_sizes = Counter()
    for location in ('assets/images/classic', 'assets/fonts/classic'):
        folder = root / location
        inventory = json.loads((folder / 'manifest.json').read_text())
        for entry in inventory['resources']:
            data = (folder / entry['path']).read_bytes()
            require(len(data) == entry['bytes'], f"Asset size: {entry['path']}")
            require(hashlib.sha256(data).hexdigest() == entry['sha256'], f"Asset checksum: {entry['path']}")
            if entry['path'].endswith('.png'):
                require(data[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid PNG')
                dimensions = struct.unpack('>II', data[16:24])
                require(dimensions == (entry['width'], entry['height']), 'Icon canvas changed')
                require(dimensions in ((16, 16), (32, 32), (48, 48)), 'Unexpected icon canvas')
                require((dimensions == (16, 16)) == entry['path'].startswith('icons/16/'), 'Small icon must be a native 16x16 source')
                require((dimensions == (32, 32)) == entry['path'].startswith('icons/32/'), 'Heading icon must be a native 32x32 source')
                icon_sizes[dimensions] += 1
            else:
                require(data[:4] == b'wOF2', 'Invalid WOFF2')
                require((folder / entry['notice']).is_file(), f"Missing font manifest notice: {entry['notice']}")
            checked += 1
    for name in ('font-regular-license.txt', 'font-bold-license.txt', 'NOTICE.md'):
        require((root / 'assets/fonts/classic' / name).is_file(), f'Missing font attribution: {name}')
    require(icon_sizes == {(48, 48): 8, (32, 32): 5, (16, 16): 7}, f'Unexpected native icon inventory: {icon_sizes}')
    require(checked == 22, f'Expected twenty icons and two fonts, got {checked}')
    return checked


def resolve(reference, current, root, baseurl):
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        return None, ''
    path = unquote(url.path)
    if path.startswith('/'):
        if baseurl:
            require(path == baseurl or path.startswith(baseurl + '/'), f'Escapes configured subpath: {reference}')
            path = path[len(baseurl):]
        target = root / path.lstrip('/')
    elif path:
        target = current.parent / path
    else:
        target = current
    if target.is_dir():
        target = target / 'index.html'
    elif not target.is_file() and not target.suffix:
        target = target.with_suffix('.html')
    require(target.is_file(), f'Missing local resource: {current.relative_to(root)} -> {reference}')
    require(target.resolve().is_relative_to(root.resolve()), f'Escapes output directory: {reference}')
    return target, unquote(url.fragment)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site_root', type=Path)
    parser.add_argument('--baseurl', default='/academic-homepage-nostalgia-1990s')
    args = parser.parse_args()
    root = args.site_root.resolve()
    baseurl = args.baseurl.rstrip('/')
    require(root.is_dir(), 'Build directory missing')
    pages = {path: Page(path.read_text()) for path in root.rglob('*.html')}
    for name in ('index.html', 'publications.html', 'blog.html', 'showcase.html', '404.html'):
        require(root / name in pages, f'Missing page: {name}')
    posts = list((REPO / '_posts').glob('*.md'))
    require(len(pages) == 5 + len(posts), 'Unexpected/missing generated pages')
    require(not (root / 'index_layout2.html').exists(), 'Layout 2 still published')
    checked_links = 0
    baseline_examples = 0
    for path, page in pages.items():
        require(page.tags['main'] == 1, f'Main landmark: {path}')
        for cls in ('classic-frame', 'classic-masthead', 'classic-navigation', 'classic-footer'):
            require(page.classes[cls] == 1, f'Inconsistent shared shell: {cls} in {path}')
        require(len(page.navigation) == 4, f'Navigation mismatch: {path}')
        expected_nav = [baseurl + suffix for suffix in ('/', '/publications', '/blog', '/showcase')]
        require([item['href'] for item in page.navigation] == expected_nav, f'Navigation URL mismatch: {path}')
        require(not any(value > 1 for value in page.ids.values()), f'Duplicate IDs: {path}')
        require(not page.classes['fixed-top'], f'Fixed header: {path}')
        require(len(page.credit_details) == 1 and 'open' not in page.credit_details[0], f'Artwork credits must be collapsed: {path}')
        require(not page.footer_icons, f'Footer icon should be removed: {path}')
        require(page.classes['classic-contact-button'] == page.classes['classic-contact-icon'] == page.classes['classic-contact-label'], f'Contact button must have an icon and label: {path}')
        for cover in page.visual_hashes:
            require(cover.get('viewbox') == '0 0 150 100' and cover.get('shape-rendering') == 'crispEdges', 'Visual hash must use the classic pixel canvas')
            require(cover.get('aria-hidden') == 'true' and cover.get('focusable') == 'false', 'Generated cover should be decorative beside its publication title')
            require(bool(cover.get('data-bubble-visual-hash')), 'Generated cover is missing its deterministic seed')
        for image in page.images:
            classes = image.get('class', '').split()
            if 'classic-research-cover' in classes:
                require(bool(image.get('alt')), 'Publication cover lacks alt text')
            if 'classic-icon' in classes:
                require(image.get('alt') == '', 'Decorative icon should have empty alt')
                require(image.get('width') == image.get('height') == '32', 'Heading icon must display at 32x32')
                target, _ = resolve(image['src'], path, root, baseurl)
                require(target is not None, 'Heading icon must be self-hosted')
                data = target.read_bytes()
                require(data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == (32, 32), 'Heading icon must be intrinsically 32x32, not downscaled artwork')
            if 'classic-contact-icon' in classes:
                require(image.get('alt') == '', 'Contact icon should be decorative beside its text label')
                require(image.get('width') == image.get('height') == '16', 'Contact icon should use a small 16px canvas')
                target, _ = resolve(image['src'], path, root, baseurl)
                require(target is not None, 'Contact icon must be self-hosted')
                data = target.read_bytes()
                require(data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == (16, 16), 'Contact icon must be intrinsically 16x16, not a downscaled larger image')
                require('help_book_small' not in image.get('src', ''), 'Help-book icon should not be used in contact links')
        for reference in page.references:
            if reference == '../blob/master/LICENSE' and path.relative_to(root).as_posix() in BASELINE_EXAMPLES:
                source_name = path.name.replace('.html', '.md')
                prefix = path.relative_to(root).parts[:3]
                post = '-'.join(prefix) + '-' + source_name
                baseline = subprocess.run(['git', 'show', 'HEAD:_posts/' + post], cwd=REPO, capture_output=True, text=True)
                require(baseline.returncode == 0 and '../blob/master/LICENSE' in baseline.stdout, 'Baseline link exception is not justified')
                baseline_examples += 1
                continue
            target, fragment = resolve(reference, path, root, baseurl)
            if target is None:
                continue
            if fragment and target in pages:
                require(fragment in pages[target].ids, f'Missing anchor: {path.name} -> {reference}')
            checked_links += 1
    publications = len(list((REPO / '_publications').rglob('*.md')))
    require(any('classic-icon' in image.get('class', '').split() and image.get('src', '').endswith('/icons/32/tree-0.png') for image in pages[root / 'index.html'].images), 'About me must use the native tree icon')
    require(pages[root / 'publications.html'].classes['classic-publication'] == publications, 'Publication lost or duplicated')
    missing_covers = sum(not re.search(r'^cover:[ \t]*\S', path.read_text(), re.M) for path in (REPO / '_publications').rglob('*.md'))
    require(len(pages[root / 'publications.html'].visual_hashes) == missing_covers, 'A coverless publication is missing its classic visual hash')
    require(pages[root / 'blog.html'].classes['classic-blog-entry'] == len(posts), 'Blog post lost or duplicated')
    showcase = sum(bool(re.search(r'^show:\s*true\s*$', path.read_text(), re.M)) for path in (REPO / '_showcase').rglob('*.md'))
    require(pages[root / 'showcase.html'].classes['grid-item'] == showcase, 'Showcase item lost or duplicated')
    news = len(list((REPO / '_news').glob('*.md')))
    require(pages[root / 'index.html'].tags['time'] == news, 'News lost or duplicated')
    for forbidden in ('_design', 'scripts', 'resources', 'index_layout2.html'):
        require(not (root / forbidden).exists(), f'Research/tool output published: {forbidden}')
    for css in ('global.css', 'blog.css'):
        source = (root / 'assets/css' / css).read_text()
        for value in re.findall(r'url\([\"\x27]?([^\)\"\x27]+)', source):
            resolve(value, root / 'assets/css' / css, root, baseurl)
    unchanged = ['_data/profile.yml', '_data/authors.yml', '_posts', '_news', '_publications', '_showcase', 'assets/images/photos', 'assets/images/covers', 'assets/images/badges']
    result = subprocess.run(['git', 'diff', '--exit-code', '--'] + unchanged, cwd=REPO, capture_output=True, text=True)
    require(result.returncode == 0, 'Existing content/images were modified')
    display_baseline = subprocess.run(['git', 'show', 'HEAD:_data/display.yml'], cwd=REPO, capture_output=True, text=True)
    require(display_baseline.returncode == 0, 'Cannot verify original display configuration')
    expected_display = display_baseline.stdout.replace('<i class="fas fa-pencil-ruler"></i> ', '', 1)
    require((REPO / '_data/display.yml').read_text() == expected_display, 'Display configuration changed beyond the requested footer icon removal')
    assets = asset_integrity(root)
    require(baseline_examples == 2, 'Unexpected baseline sample-link count')
    print(f'PASS: {len(pages)} pages; {checked_links} local references; {publications} papers; {len(posts)} posts; {showcase} showcase items; {news} news items; {assets} unchanged classic assets; content preserved; research excluded. Baseurl: {baseurl or "/"}')
    print('KNOWN BASELINE: two unchanged sample-blog ../blob/master/LICENSE links are not valid website links; excluded with git HEAD evidence.')


if __name__ == '__main__':
    main()
