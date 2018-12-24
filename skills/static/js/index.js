$('.entry-header').click(function() {
    $('.entry-expand').slideUp();
    if ($(this).next('.entry-expand').is(':hidden'))
	    $(this).next('.entry-expand').slideDown();
});
