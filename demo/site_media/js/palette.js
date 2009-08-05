/* jQuery helper to render palette views */

$(function () {
    $(".palette_list .colour_box").each(function (i) {
        var box = $(this);
        var count = box.length;

        box.children().each(function (i) {
            $(this)
              .width(box.width() / count)
              .css("background-color", $(this).text())
              .html('&thinsp;');
        });
    });
});

