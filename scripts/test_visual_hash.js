'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const filename = require.resolve('../assets/js/bubble_visual_hash.js');
const {buildVisualHash} = require(filename);
const seeds = ['', 'abc', 'Publication without cover image', 'Café: α + β', '研究 😀', '<script>alert(1)</script>'];
const colors = new Set(['#dfdfdf', '#c0c0c0', '#808080', '#ffffff', '#000080', '#1084d0', '#000040', '#008080', '#00ffff', '#004040', '#800080', '#ff00ff', '#400040', '#808000', '#ffff00', '#404000']);

assert.equal(buildVisualHash('abc').fingerprint, '900150983cd24fb0d6963f7d28e17f72');
for (const seed of seeds) {
    const model = buildVisualHash(seed);
    assert.deepEqual(model, buildVisualHash(seed), 'Same seed must produce exactly the same cover');
    assert.equal(model.width, 150);
    assert.equal(model.height, 100);
    assert.equal(model.layers.length, 14, 'Background plus six shadow/bubble pairs');
    for (const layer of model.layers) {
        assert.ok(layer.pixels.length > 0);
        for (const pixel of layer.pixels) {
            assert.ok([pixel.x, pixel.y, pixel.width, pixel.height].every(n => Number.isInteger(n) && n % 2 === 0));
            assert.ok(pixel.width > 0 && pixel.height > 0);
            assert.ok(pixel.x >= 0 && pixel.y >= 0 && pixel.x + pixel.width <= 150 && pixel.y + pixel.height <= 100);
            assert.ok(colors.has(pixel.fill), 'Only opaque classic palette colors');
        }
    }
}
const fingerprints = new Set(Array.from({length: 128}, (_, i) => buildVisualHash('Paper ' + i).fingerprint));
assert.equal(fingerprints.size, 128);
assert.notDeepEqual(buildVisualHash('Paper A').layers, buildVisualHash('Paper B').layers);

// Exercise the DOM writer with a small fake document, not a browser instance.
const svg = {
    attrs: {'data-bubble-visual-hash': '<script>alert(1)</script>'},
    children: [],
    getAttribute(name) { return this.attrs[name]; },
    setAttribute(name, value) { this.attrs[name] = value; },
    replaceChildren(fragment) { this.children = fragment.children; }
};
const document = {
    querySelectorAll() { return [svg]; },
    createDocumentFragment() { return {children: [], appendChild(child) { this.children.push(child); }}; },
    createElementNS(namespace, tag) {
        assert.equal(namespace, 'http://www.w3.org/2000/svg');
        assert.equal(tag, 'path');
        return {attrs: {}, setAttribute(name, value) { this.attrs[name] = value; }};
    }
};
const source = fs.readFileSync(filename, 'utf8');
vm.runInNewContext(source, {document});
assert.match(svg.attrs['data-visual-hash-rendered'], /^[0-9a-f]{32}$/);
assert.ok(svg.children.length > 20 && svg.children.length <= 38, 'Pixels should be batched into a few dozen SVG paths');
for (const path of svg.children) {
    assert.ok(colors.has(path.attrs.fill));
    assert.match(path.attrs.d, /^[Mhvz0-9 -]+$/);
}
const firstRender = JSON.stringify(svg.children);
vm.runInNewContext(source, {document});
assert.equal(JSON.stringify(svg.children), firstRender, 'Rerender must replace, not duplicate, the pattern');
console.log('PASS: deterministic seeds; classic palette; bounded 2px grid; Unicode/input safety; batched SVG paths; idempotent rendering.');
