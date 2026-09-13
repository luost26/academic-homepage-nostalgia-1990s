(function () {
    var toc = document.getElementById('blog-toc');
    var tocList = document.querySelector('.blog-toc-list');
    var content = document.querySelector('.blog-content');
    if (!toc || !tocList || !content) return;
    var headings = content.querySelectorAll('h1, h2, h3');
    if (!headings.length) { toc.hidden = true; return; }
    headings.forEach(function (heading, index) {
        if (!heading.id) heading.id = 'article-section-' + index;
        var li = document.createElement('li');
        var link = document.createElement('a');
        link.href = '#' + heading.id;
        link.textContent = heading.textContent;
        link.className = 'toc-' + heading.tagName.toLowerCase();
        li.appendChild(link);
        tocList.appendChild(li);
    });
    var links = tocList.querySelectorAll('a');
    function updateActive() {
        var current = headings[0].id;
        headings.forEach(function (heading) {
            if (heading.getBoundingClientRect().top <= 24) current = heading.id;
        });
        links.forEach(function (link) {
            var active = link.hash === '#' + current;
            link.classList.toggle('toc-active', active);
            if (active) link.setAttribute('aria-current', 'location');
            else link.removeAttribute('aria-current');
        });
    }
    var pending = false;
    window.addEventListener('scroll', function () {
        if (pending) return;
        pending = true;
        requestAnimationFrame(function () { updateActive(); pending = false; });
    }, {passive: true});
    window.addEventListener('hashchange', updateActive);
    var narrow = matchMedia('(max-width: 991px)');
    function setDisclosure() { toc.open = !narrow.matches; }
    setDisclosure();
    narrow.addEventListener('change', setDisclosure);
    document.addEventListener('DOMContentLoaded', function () {
        if (typeof Prism !== 'undefined') Prism.highlightAll();
        updateActive();
    });
    if (document.fonts) document.fonts.ready.then(updateActive);
    updateActive();
})();
