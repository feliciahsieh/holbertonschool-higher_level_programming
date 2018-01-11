#!/usr/bin/node
// Must install module, sync-request with
// $npm install sync-request

let args = process.argv.slice(2);
if (args[0] === undefined) { // No user argument
  process.exit();
} else if (args.length !== 1) {
  process.exit();
}

let base = 'http://swapi.co/api/films/' + args[0];

var request = require('request');
var request = require('sync-request');

try {
  let res = request('GET', base);

  let obj = res.getBody();
  let obj2 = JSON.parse(obj);
  let characters = obj2['characters'];

  for (let i = 0; i < characters.length; i++) {
    let resCharacter = request('GET', characters[i]);

    let c = resCharacter.getBody();
    let cJson = JSON.parse(c);
    console.log(cJson['name']);
  }
} catch (e) {}
