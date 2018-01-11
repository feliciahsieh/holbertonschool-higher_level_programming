#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] === undefined) {
  process.exit();
} else if (args.length !== 1) {
  process.exit();
}

let url = args[0];
let IdWedge = 'https://swapi.co/api/people/18/';
let request = require('request');
request(url, function (error, response, body) {
  if (error) { // Handle error if one occurred
  }
  if (response.statusCode === 200) {
    let count = 0;
    let obj = JSON.parse(body);

    for (let i = 0; i < obj['results'].length; i++) {
      for (let j = 0; j < obj['results'][i]['characters'].length; j++) {
        if (obj['results'][i]['characters'][j] === IdWedge) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(response.statusCode);
  }
});
