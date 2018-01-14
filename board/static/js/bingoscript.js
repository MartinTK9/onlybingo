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
//buttons landing
   $('#create').on('click', event => {
		$('.cardpage').removeClass('hide');
		$('.landing').addClass('hide');
   	});

	 $('#highsco').on('click', event => {
		$('.highsco').removeClass('hide');
		$('.landing').addClass('hide');
   	});

//back buttons
	$('#backhigh').on('click', event => {
		$('.highsco').addClass('hide');
		$('.landing').removeClass('hide');
   	});

	$('#backcard').on('click', event => {
		$('.cardpage').addClass('hide');
		$('.landing').removeClass('hide');
   	});

	$('#backjoin').on('click', event => {
		$('.joinpage').addClass('hide');
		$('.landing').removeClass('hide');
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
