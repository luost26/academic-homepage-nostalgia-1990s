// aHR0cHM6Ly9naXRodWIuY29tL2x1b3N0MjYvYWNhZGVtaWMtaG9tZXBhZ2U=
$(function () {
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var lazyLoadOptions = {
        scrollDirection: 'vertical',
        effect: reducedMotion ? 'show' : 'fadeIn',
        effectTime: reducedMotion ? 0 : 300,
        placeholder: "",
        onError: function(element) {
            console.log('[lazyload] Error loading ' + element.data('src'));
        },
        afterLoad: function(element) {
            if (element.is('img')) {
                // remove background-image style
                element.css('background-image', 'none');
                element.css('min-height', '0');
            } else if (element.is('div')) {
                // set the style to background-size: cover; 
                element.css('background-size', 'cover');
                element.css('background-position', 'center');
            }
        }
    }

    $('img.lazy, div.lazy:not(.always-load)').Lazy({visibleOnly: true, ...lazyLoadOptions});
    $('div.lazy.always-load').Lazy({visibleOnly: false, ...lazyLoadOptions});

    $('[data-toggle="tooltip"]').tooltip()

    $('.carousel').on('slid.bs.carousel', function () {
        $(this).find('[data-slide-to]').each(function () {
            this.setAttribute('aria-pressed', this.classList.contains('active') ? 'true' : 'false');
        });
        if ($grid) $grid.masonry('layout');
    });

    var $grid = $('.grid').masonry({
        "percentPosition": true,
        "itemSelector": ".grid-item",
        "columnWidth": ".grid-sizer"
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });
    if (document.fonts) {
        document.fonts.ready.then(function () { $grid.masonry('layout'); });
    }

    $(".lazy").on("load", function () {
        $grid.masonry('layout');
    });
})
