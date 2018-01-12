$('#toggle_header').click(function () {
  $('header').toggleClass(function() {
    if ( $('header').is('green')) {
      return 'red';
    } else {
      return 'green';
    }
    $('header').removeClass();
  });
});
