var $win = $(window),
    w = 0,h = 0,
    rgb = [],
    getWidth = function() {
        w = $win.width();
        h = $win.height();
    };

$win.resize(getWidth).mousemove(function(e) {
    
    rgb = [
        Math.round(e.pageX/w * 255),
        Math.round(e.pageY/h * 255),
        150
    ];
    
    $("#left").css('background','rgb('+rgb.join(',')+')');
        $("#right").css('background','rgb('+rgb.join(',')+')');
    $("#top").css('background','rgb('+rgb.join(',')+')');
    $("bottom").css('background','rgb('+rgb.join(',')+')');

}).resize()



