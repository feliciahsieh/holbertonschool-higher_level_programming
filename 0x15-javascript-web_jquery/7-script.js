let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url)
  .done(function (data) {
    console.log(data['name']);
    $('header').replaceWith(data['name']);
  });
