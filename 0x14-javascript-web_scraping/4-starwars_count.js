#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 1) {
  process.exit();
}

let IDWedgeAntilles = 18;
let urlbase = 'http://swapi.co/api/' + 'people/' + IDWedgeAntilles;
let request = require('request');

request(urlbase, function (error, response, body) {
  if (error) {
    // Handle error if one occurred
  }
  // console.log('code:', response && response.statusCode); // Print response status code if a response was received
  if (response.statusCode === 200) {
    let obj = JSON.parse(body);
    console.log(obj['films'].length);
  } else {
    console.log('HTTP err:' + response.statusCode);
  }
});
