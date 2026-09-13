//  Formatted version of a popular md5 implementation
//  Original copyright (c) Paul Johnston & Greg Holt.
function md5(inputString) {
    var hc = "0123456789abcdef";
    function rh(n) { var j, s = ""; for (j = 0; j <= 3; j++) s += hc.charAt((n >> (j * 8 + 4)) & 0x0F) + hc.charAt((n >> (j * 8)) & 0x0F); return s; }
    function ad(x, y) { var l = (x & 0xFFFF) + (y & 0xFFFF); var m = (x >> 16) + (y >> 16) + (l >> 16); return (m << 16) | (l & 0xFFFF); }
    function rl(n, c) { return (n << c) | (n >>> (32 - c)); }
    function cm(q, a, b, x, s, t) { return ad(rl(ad(ad(a, q), ad(x, t)), s), b); }
    function ff(a, b, c, d, x, s, t) { return cm((b & c) | ((~b) & d), a, b, x, s, t); }
    function gg(a, b, c, d, x, s, t) { return cm((b & d) | (c & (~d)), a, b, x, s, t); }
    function hh(a, b, c, d, x, s, t) { return cm(b ^ c ^ d, a, b, x, s, t); }
    function ii(a, b, c, d, x, s, t) { return cm(c ^ (b | (~d)), a, b, x, s, t); }
    function sb(x) {
        var i; var nblk = ((x.length + 8) >> 6) + 1; var blks = new Array(nblk * 16); for (i = 0; i < nblk * 16; i++) blks[i] = 0;
        for (i = 0; i < x.length; i++) blks[i >> 2] |= x.charCodeAt(i) << ((i % 4) * 8);
        blks[i >> 2] |= 0x80 << ((i % 4) * 8); blks[nblk * 16 - 2] = x.length * 8; return blks;
    }
    var i, x = sb("" + inputString), a = 1732584193, b = -271733879, c = -1732584194, d = 271733878, olda, oldb, oldc, oldd;
    for (i = 0; i < x.length; i += 16) {
        olda = a; oldb = b; oldc = c; oldd = d;
        a = ff(a, b, c, d, x[i + 0], 7, -680876936); d = ff(d, a, b, c, x[i + 1], 12, -389564586); c = ff(c, d, a, b, x[i + 2], 17, 606105819);
        b = ff(b, c, d, a, x[i + 3], 22, -1044525330); a = ff(a, b, c, d, x[i + 4], 7, -176418897); d = ff(d, a, b, c, x[i + 5], 12, 1200080426);
        c = ff(c, d, a, b, x[i + 6], 17, -1473231341); b = ff(b, c, d, a, x[i + 7], 22, -45705983); a = ff(a, b, c, d, x[i + 8], 7, 1770035416);
        d = ff(d, a, b, c, x[i + 9], 12, -1958414417); c = ff(c, d, a, b, x[i + 10], 17, -42063); b = ff(b, c, d, a, x[i + 11], 22, -1990404162);
        a = ff(a, b, c, d, x[i + 12], 7, 1804603682); d = ff(d, a, b, c, x[i + 13], 12, -40341101); c = ff(c, d, a, b, x[i + 14], 17, -1502002290);
        b = ff(b, c, d, a, x[i + 15], 22, 1236535329); a = gg(a, b, c, d, x[i + 1], 5, -165796510); d = gg(d, a, b, c, x[i + 6], 9, -1069501632);
        c = gg(c, d, a, b, x[i + 11], 14, 643717713); b = gg(b, c, d, a, x[i + 0], 20, -373897302); a = gg(a, b, c, d, x[i + 5], 5, -701558691);
        d = gg(d, a, b, c, x[i + 10], 9, 38016083); c = gg(c, d, a, b, x[i + 15], 14, -660478335); b = gg(b, c, d, a, x[i + 4], 20, -405537848);
        a = gg(a, b, c, d, x[i + 9], 5, 568446438); d = gg(d, a, b, c, x[i + 14], 9, -1019803690); c = gg(c, d, a, b, x[i + 3], 14, -187363961);
        b = gg(b, c, d, a, x[i + 8], 20, 1163531501); a = gg(a, b, c, d, x[i + 13], 5, -1444681467); d = gg(d, a, b, c, x[i + 2], 9, -51403784);
        c = gg(c, d, a, b, x[i + 7], 14, 1735328473); b = gg(b, c, d, a, x[i + 12], 20, -1926607734); a = hh(a, b, c, d, x[i + 5], 4, -378558);
        d = hh(d, a, b, c, x[i + 8], 11, -2022574463); c = hh(c, d, a, b, x[i + 11], 16, 1839030562); b = hh(b, c, d, a, x[i + 14], 23, -35309556);
        a = hh(a, b, c, d, x[i + 1], 4, -1530992060); d = hh(d, a, b, c, x[i + 4], 11, 1272893353); c = hh(c, d, a, b, x[i + 7], 16, -155497632);
        b = hh(b, c, d, a, x[i + 10], 23, -1094730640); a = hh(a, b, c, d, x[i + 13], 4, 681279174); d = hh(d, a, b, c, x[i + 0], 11, -358537222);
        c = hh(c, d, a, b, x[i + 3], 16, -722521979); b = hh(b, c, d, a, x[i + 6], 23, 76029189); a = hh(a, b, c, d, x[i + 9], 4, -640364487);
        d = hh(d, a, b, c, x[i + 12], 11, -421815835); c = hh(c, d, a, b, x[i + 15], 16, 530742520); b = hh(b, c, d, a, x[i + 2], 23, -995338651);
        a = ii(a, b, c, d, x[i + 0], 6, -198630844); d = ii(d, a, b, c, x[i + 7], 10, 1126891415); c = ii(c, d, a, b, x[i + 14], 15, -1416354905);
        b = ii(b, c, d, a, x[i + 5], 21, -57434055); a = ii(a, b, c, d, x[i + 12], 6, 1700485571); d = ii(d, a, b, c, x[i + 3], 10, -1894986606);
        c = ii(c, d, a, b, x[i + 10], 15, -1051523); b = ii(b, c, d, a, x[i + 1], 21, -2054922799); a = ii(a, b, c, d, x[i + 8], 6, 1873313359);
        d = ii(d, a, b, c, x[i + 15], 10, -30611744); c = ii(c, d, a, b, x[i + 6], 15, -1560198380); b = ii(b, c, d, a, x[i + 13], 21, 1309151649);
        a = ii(a, b, c, d, x[i + 4], 6, -145523070); d = ii(d, a, b, c, x[i + 11], 10, -1120210379); c = ii(c, d, a, b, x[i + 2], 15, 718787259);
        b = ii(b, c, d, a, x[i + 9], 21, -343485551); a = ad(a, olda); b = ad(b, oldb); c = ad(c, oldc); d = ad(d, oldd);
    }
    return rh(a) + rh(b) + rh(c) + rh(d);
}


// Classic pixel-bubble renderer, retaining the original MD5 visual seed.
(function () {
    'use strict';
    var WIDTH = 150;
    var HEIGHT = 100;
    var PIXEL = 2;
    var PALETTES = [
        {fill: '#000080', light: '#1084d0', dark: '#000040'},
        {fill: '#008080', light: '#00ffff', dark: '#004040'},
        {fill: '#800080', light: '#ff00ff', dark: '#400040'},
        {fill: '#808000', light: '#ffff00', dark: '#404000'}
    ];

    // A visual fingerprint only: no randomness, animation, or network requests.
    function buildVisualHash(seed) {
        var hash = md5(String(seed));
        var digits = hash.split('').map(function (digit) { return parseInt(digit, 16); });
        var layers = [{pixels: [{x: 0, y: 0, width: WIDTH, height: HEIGHT, fill: '#dfdfdf'}]}];
        var dots = [];
        for (var y = 2; y < HEIGHT; y += 10) {
            for (var x = 2; x < WIDTH; x += 10) dots.push({x: x, y: y, width: PIXEL, height: PIXEL, fill: '#c0c0c0'});
        }
        layers.push({pixels: dots});
        var bubbles = [];
        for (var i = 0; i < 6; i++) {
            bubbles.push({
                x: 14 + digits[i * 2] * 8,
                y: 12 + digits[i * 2 + 1] * 4,
                radius: 10 + digits[14 + i] * 2,
                palette: PALETTES[digits[22 + i] % PALETTES.length]
            });
        }
        bubbles.sort(function (a, b) { return b.radius - a.radius; });
        bubbles.forEach(function (bubble) {
            var shadow = [];
            var pixels = [];
            var radius = bubble.radius;
            function inside(dx, dy) { return dx * dx + dy * dy <= radius * radius; }
            function add(target, x, y, fill) {
                if (x < 0 || y < 0 || x + PIXEL > WIDTH || y + PIXEL > HEIGHT) return;
                target.push({x: x, y: y, width: PIXEL, height: PIXEL, fill: fill});
            }
            for (var dy = -radius; dy <= radius; dy += PIXEL) {
                for (var dx = -radius; dx <= radius; dx += PIXEL) {
                    if (!inside(dx + 1, dy + 1)) continue;
                    var edge = !inside(dx - 1, dy + 1) || !inside(dx + 3, dy + 1) ||
                        !inside(dx + 1, dy - 1) || !inside(dx + 1, dy + 3);
                    var checker = ((dx + dy + radius * 2) / PIXEL) % 2 === 0;
                    var fill = bubble.palette.fill;
                    if (edge) fill = bubble.palette.dark;
                    else if (dx + dy < -radius * 0.6) fill = checker ? '#ffffff' : bubble.palette.light;
                    else if (dx + dy < 0) fill = checker ? bubble.palette.light : bubble.palette.fill;
                    else if (dx + dy > radius * 0.6) fill = checker ? bubble.palette.dark : bubble.palette.fill;
                    add(shadow, bubble.x + dx + PIXEL, bubble.y + dy + PIXEL, '#808080');
                    add(pixels, bubble.x + dx, bubble.y + dy, fill);
                }
            }
            layers.push({pixels: shadow}, {pixels: pixels});
        });
        return {width: WIDTH, height: HEIGHT, fingerprint: hash, layers: layers};
    }

    function render(svg) {
        var model = buildVisualHash(svg.getAttribute('data-bubble-visual-hash') || 'publication');
        var namespace = 'http://www.w3.org/2000/svg';
        var fragment = document.createDocumentFragment();
        // Merge same-color pixels within each layer, preserving overlap order.
        // A cover has a few dozen paths, not thousands of DOM pixel elements.
        model.layers.forEach(function (layer) {
            var colors = {};
            layer.pixels.forEach(function (pixel) {
                if (!colors[pixel.fill]) colors[pixel.fill] = [];
                colors[pixel.fill].push('M' + pixel.x + ' ' + pixel.y + 'h' + pixel.width + 'v' + pixel.height + 'h-' + pixel.width + 'z');
            });
            Object.keys(colors).forEach(function (fill) {
                var path = document.createElementNS(namespace, 'path');
                path.setAttribute('fill', fill);
                path.setAttribute('d', colors[fill].join(''));
                fragment.appendChild(path);
            });
        });
        svg.replaceChildren(fragment);
        svg.setAttribute('data-visual-hash-rendered', model.fingerprint);
    }

    if (typeof module !== 'undefined' && module.exports) module.exports = {buildVisualHash: buildVisualHash};
    if (typeof document === 'undefined') return;
    document.querySelectorAll('.bubble-visual-hash').forEach(render);
})();
