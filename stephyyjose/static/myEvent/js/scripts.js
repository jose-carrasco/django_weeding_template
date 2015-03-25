$(document).ready(function() {

	$("#register").submit( function (event) {
        event.preventDefault();
        $('.message p').empty();
        $.ajax({
            method: "POST",
            url: '/register',
            dataType: 'json',
            data: $('#register').serialize()
		}).done(function (data) {
				alert("mensaje");
        	});
    });



	// Smooth scrolling navigation

		$(".scroll").click(function(event){		
			event.preventDefault();
			$('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
		});

	
	
	// Turn parallax scrolling off for iOS devices
	var iOS = false,
    p = navigator.platform;

	if( p === 'iPad' || p === 'iPhone' || p === 'iPod' ){
		iOS = true;
	}


	// Scroll effect on Home Page box
	if(iOS == false){
		var div = $('#main-title-text');
				$(window).on('scroll', function() {
				   var st = $(this).scrollTop();
				   div.css({ 'opacity' : (1 - st/400) });
				   div.css({ 'top' : (st*1.3) });
				});
	}
			
			
	// Initialize fancybox (lightbox plugin)
	$('.fancybox').fancybox();



	//Code for countdown timer
	$(".kkcount-down").kkcountdown({
		dayText		: '',
		daysText 	: ' días ',
		hoursText	: ':',
		minutesText	: ':',
		secondsText	: '',
		displayZeroDays : false,
		addClass	: ''
	});

	 
	 










});
