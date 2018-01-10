#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 1) {
  process.exit();
}

let url = args[0];
let request = require('request');
request(url, function (error, response, body) {
  if (error) {
    // Handle error if one occurred
  }
  if (response.statusCode === 200) {
    let obj = JSON.parse(body);
    let d = {};
    console.log(body);
    obj.forEach(function (element) {
      console.log('element:' + element['id'] + 'd[uid]:"' + d[element['userId']]);
      if (d[element['userId']] === undefined) {
        d[element['userId']] = 1;
      } else {
        d[element['userId']]++;
      }
    });
    console.log(d);
  }
});
