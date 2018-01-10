#!/usr/bin/node

let fs = require('fs');
var content, content2;

fs.readFile('./fileA', function read (err, data) {
  if (err) {
    throw err;
  }
  content = data;
});

fs.readFile('./fileB', function read (err, data2) {
  if (err) {
    throw err;
  }
  content2 = data2;
  processFile();
});

function processFile () {
  let contentTotal = content + content2;
  fs.writeFile('./fileC', contentTotal, 'utf8', function (err) {
    if (err) {
      throw err;
    }
  }
  );
}
