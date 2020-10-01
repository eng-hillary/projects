
// Prepare demo data
// Data is joined to map using value of 'hc-key' property by default.
// See API docs for 'joinBy' for more info on linking data and map.
var data = [
    ['ug-2595', 0],
    ['ug-7073', 1],
    ['ug-7074', 2],
    ['ug-7075', 3],
    ['ug-2785', 4],
    ['ug-2791', 5],
    ['ug-3385', 6],
    ['ug-3388', 7],
    ['ug-2786', 8],
    ['ug-7056', 9],
    ['ug-7083', 10],
    ['ug-7084', 11],
    ['ug-7058', 12],
    ['ug-1678', 13],
    ['ug-1682', 14],
    ['ug-1683', 15],
    ['ug-1685', 16],
    ['ug-7051', 17],
    ['ug-2762', 18],
    ['ug-2767', 19],
    ['ug-2777', 20],
    ['ug-2778', 21],
    ['ug-2780', 22],
    ['ug-2781', 23],
    ['ug-2782', 24],
    ['ug-2783', 25],
    ['ug-2779', 26],
    ['ug-2784', 27],
    ['ug-3382', 28],
    ['ug-3384', 29],
    ['ug-3389', 30],
    ['ug-3383', 31],
    ['ug-3390', 32],
    ['ug-3386', 33],
    ['ug-3391', 34],
    ['ug-3392', 35],
    ['ug-3394', 36],
    ['ug-2750', 37],
    ['ug-7048', 38],
    ['ug-7080', 39],
    ['ug-7081', 40],
    ['ug-1684', 41],
    ['ug-7082', 42],
    ['ug-1688', 43],
    ['ug-7079', 44],
    ['ug-7068', 45],
    ['ug-7070', 46],
    ['ug-7049', 47],
    ['ug-2787', 48],
    ['ug-7055', 49],
    ['ug-2769', 50],
    ['ug-7052', 51],
    ['ug-2774', 52],
    ['ug-7059', 53],
    ['ug-7060', 54],
    ['ug-7057', 55],
    ['ug-2790', 56],
    ['ug-2776', 57],
    ['ug-7067', 58],
    ['ug-7065', 59],
    ['ug-7066', 60],
    ['ug-7069', 61],
    ['ug-7061', 62],
    ['ug-7063', 63],
    ['ug-7062', 64],
    ['ug-7064', 65],
    ['ug-7086', 66],
    ['ug-2744', 67],
    ['ug-1679', 68],
    ['ug-1680', 69],
    ['ug-7054', 70],
    ['ug-1686', 71],
    ['ug-7078', 72],
    ['ug-1677', 73],
    ['ug-1690', 74],
    ['ug-2745', 75],
    ['ug-2752', 76],
    ['ug-2754', 77],
    ['ug-1687', 78],
    ['ug-2757', 79],
    ['ug-1689', 80],
    ['ug-2760', 81],
    ['ug-2761', 82],
    ['ug-2766', 83],
    ['ug-2765', 84],
    ['ug-2764', 85],
    ['ug-2749', 86],
    ['ug-2768', 87],
    ['ug-2763', 88],
    ['ug-2748', 89],
    ['ug-2771', 90],
    ['ug-2772', 91],
    ['ug-2775', 92],
    ['ug-2788', 93],
    ['ug-2789', 94],
    ['ug-3381', 95],
    ['ug-3387', 96],
    ['ug-3393', 97],
    ['ug-7076', 98],
    ['ug-1681', 99],
    ['ug-2746', 100],
    ['ug-2747', 101],
    ['ug-2751', 102],
    ['ug-2758', 103],
    ['ug-2759', 104],
    ['ug-2756', 105],
    ['ug-2770', 106],
    ['ug-7072', 107],
    ['ug-7053', 108],
    ['ug-2753', 109],
    ['ug-2755', 110],
    ['ug-2773', 111]
];

// Create the chart
Highcharts.mapChart('container', {
    chart: {
        map: 'countries/ug/ug-all'
    },

    title: {
        text: 'Farmer Locations'
    },

    subtitle: {
        text: 'Source map: <a href="https://code.highcharts.com/mapdata/countries/ug/ug-all.js">Uganda</a>'
    },

    mapNavigation: {
        enabled: true,
        buttonOptions: {
            verticalAlign: 'bottom'
        }
    },

    colorAxis: {
        min: 0
    },

    series: [{
        data: data,
        name: 'Random data',
        states: {
            hover: {
                color: ' #228B22'
            }
        },
        dataLabels: {
            enabled: true,
            format: '{point.name}'
        }
    }]
});




(function($) {
    "use strict";
    $(".mobile-toggle").click(function(){
        $(".nav-menus").toggleClass("open");
    });
    $(".mobile-search").click(function(){
        $(".form-control-plaintext").toggleClass("open");
    });
    $(".form-control-plaintext").keyup(function(e){
        if(e.target.value) {
            $("body").addClass("offcanvas");
        } else {
            $("body").removeClass("offcanvas");
        }
    });
})(jQuery);

$('.loader-wrapper').fadeOut('slow', function() {
    $(this).remove();
});

$(window).on('scroll', function() {
    if ($(this).scrollTop() > 600) {
        $('.tap-top').fadeIn();
    } else {
        $('.tap-top').fadeOut();
    }
});
$('.tap-top').click( function() {
    $("html, body").animate({
        scrollTop: 0
    }, 600);
    return false;
});

function toggleFullScreen() {
    if ((document.fullScreenElement && document.fullScreenElement !== null) ||
        (!document.mozFullScreen && !document.webkitIsFullScreen)) {
        if (document.documentElement.requestFullScreen) {
            document.documentElement.requestFullScreen();
        } else if (document.documentElement.mozRequestFullScreen) {
            document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullScreen) {
            document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
        }
    } else {
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        }
    }
}
(function($, window, document, undefined) {
    "use strict";
    var $ripple = $(".js-ripple");
    $ripple.on("click.ui.ripple", function(e) {
        var $this = $(this);
        var $offset = $this.parent().offset();
        var $circle = $this.find(".c-ripple__circle");
        var x = e.pageX - $offset.left;
        var y = e.pageY - $offset.top;
        $circle.css({
            top: y + "px",
            left: x + "px"
        });
        $this.addClass("is-active");
    });
    $ripple.on(
        "animationend webkitAnimationEnd oanimationend MSAnimationEnd",
        function(e) {
            $(this).removeClass("is-active");
        });
})(jQuery, window, document);

$(".chat-menu-icons .toogle-bar").click(function(){
    $(".chat-menu").toggleClass("show");
});


/*=====================
 05. Image to background js
 ==========================*/
$(".bg-img" ).parent().addClass('bg-size');

jQuery('.bg-img').each(function() {

    var el = $(this),
        src = el.attr('src'),
        parent = el.parent();

    parent.css({
        'background-image': 'url(' + src + ')',
        'background-size': 'cover',
        'background-position': 'center',
        'display' : 'block'
    });

    el.hide();
});

// Avatar Switcher
function avatarSwitcher() {
    var readURL = function (input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('.profile-pic').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    };

    $(".file-upload").on('change', function () {
        readURL(this);
    });

    $(".upload-button").on('click', function () {
        $(".file-upload").click();
    });
}

avatarSwitcher();

//stepwise validation
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
// This function will display the specified tab of the form ...
var x = document.getElementsByClassName("tab-pane");
x[n].style.display = "block";
// ... and fix the Previous/Next buttons:
if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
} else {
    document.getElementById("prevBtn").style.display = "inline";
}
if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
} else {
    document.getElementById("nextBtn").innerHTML = "Next";
}
// ... and run a function that displays the correct step indicator:
fixStepIndicator(n)
}

function nextPrev(n) {
// This function will figure out which tab to display
var x = document.getElementsByClassName("tab-pane");
// Exit the function if any field in the current tab is invalid:
if (n == 1 && !validateForm()) return false;
// Hide the current tab:
x[currentTab].style.display = "none";
// Increase or decrease the current tab by 1:
currentTab = currentTab + n;
// if you have reached the end of the form... :
if (currentTab >= x.length) {
    //...the form gets submitted:
    document.getElementById("form").submit();
    return false;
}
// Otherwise, display the correct tab:
showTab(currentTab);
}

function validateForm() {
// This function deals with validation of the form fields
var x, y, i, valid = true;
x = document.getElementsByClassName("tab-pane");
y = x[currentTab].getElementsByTagName("input");
// A loop that checks every input field in the current tab:
for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
    // add an "invalid" class to the field:
    y[i].className += " invalid";
    // and set the current valid status to false:
    valid = false;
    }
}
// If the valid status is true, mark the step as finished and valid:
if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
}
return valid; // return the valid status
}

function fixStepIndicator(n) {
// This function removes the "active" class of all steps...
var i, x = document.getElementsByClassName("step");
for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
}
//... and adds the "active" class to the current step:
x[n].className += " active";
}
