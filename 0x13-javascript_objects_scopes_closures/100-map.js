#!/usr/bin/node

let count = 0;

const { list } = require('./100-data');
console.log(list);

function multFactor (num) {
  let n = num * count;
  count++;
  return n;
}

const map1 = list.map(multFactor);
console.log(map1);
