let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url)
  .done(function (data) {
    $('header').replaceWith(data['name']);
  });
