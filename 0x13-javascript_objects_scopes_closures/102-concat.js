#!/usr/bin/node

let args = process.argv.slice(2);
let f1;
let f2;
let f3;
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length === 3) {
  f1 = args[0];
  f2 = args[1];
  f3 = args[2];
} else {
  process.exit();
}

let fs = require('fs');
let content, content2;

fs.readFile(f1, function read (err, data) {
  if (err) {
    throw err;
  }
  content = data;
});

fs.readFile(f2, function read (err, data2) {
  if (err) {
    throw err;
  }
  content2 = data2;
  processFile();
});

function processFile () {
  let contentTotal = content + content2;
  fs.writeFile(f3, contentTotal, 'utf8', function (err) {
    if (err) {
      throw err;
    }
  }
  );
}
