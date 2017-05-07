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