$( ".cross" ).hide();
$( "nav" ).hide();
$( ".hamburger" ).click(function() {
    $( "nav" ).slideToggle( "slow", function() {
        $( ".hamburger" ).hide();
        $( ".cross" ).show();
    });
});

$( ".cross" ).click(function() {
    $( "nav" ).slideToggle( "slow", function() {
        $( ".cross" ).hide();
        $( ".hamburger" ).show();
    });
});

$('.dropdown-toggle').dropdown();

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});

$(window).scroll(function(){
    $(".hero").css("opacity", 1 - $(window).scrollTop() / 350);
});

var myEvent = {id: calEvent.id, start: calEvent.start, end: calEvent.end,
               allDay: calEvent.allDay };
$.ajax({
    url: 'https://www.gate15.be/srv/content/d/content-type/10/start/0/limit/50/excluded_tags/trots',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: $.toJSON(myEvent),
    dataType: 'text',
    success: function(result) {
        alert(result.Result);
    }
});