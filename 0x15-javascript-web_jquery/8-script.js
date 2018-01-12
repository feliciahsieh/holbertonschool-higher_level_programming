let url = 'https://swapi.co/api/films/?format=json';
$.get(url)
  .done(function (data) {
    console.log(data['results']['title']);

    for (let i = 0; i < data['count']; i++) {
      let title = '<li>' + data['results'][i]['title'] + '</li>';
      $('#list_movies').append(title);
    }
  });
