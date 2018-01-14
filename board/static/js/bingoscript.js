$(document).ready(() => {
	$('#free').addClass('pressed');

//bingo card
	$('.pressed').on('click', event => {
		$(event.currentTarget).toggleClass('unpressed');
   	});

   $('#free').on('click', event => {
		$(event.currentTarget).toggleClass('unpressed');
   	});

   $('.unpressed').on('click', event => {
		$(event.currentTarget).toggleClass('pressed');
   	});

//other buttons
	$('#join').on('click', event => {
		$('.cardpage').removeClass('hide');
		$('.joinpage').addClass('hide');
   	});

// setting cursor
	$('.pressed').css('cursor', 'pointer');
	$('.unpressed').css('cursor', 'pointer');




});
