//FOundation Inicializer

$(document).foundation({
"magellan-expedition": {
  active_class: 'active', // specify the class used for active sections
  threshold: 10 , // how many pixels until the magellan bar sticks, 0 = auto
  destination_threshold: 20, // pixels from the top of destination for it to be considered active
  throttle_delay: 50, // calculation throttling to increase framerate
  fixed_top: 72, // top distance in pixels assigned to the fixed element on scroll
}
});

$(document).ready( function() {
    $('.menu').smint({
        'scrollSpeed' : 1000
    });
});