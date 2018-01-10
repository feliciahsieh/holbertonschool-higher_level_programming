#!/usr/bin/node

require('./100-data');
let count = 0;

//let list = [1, 2, 3, 4, 5];
const l1 = list;
console.log(list);

function multFactor (num) {
  let n = num * count;
  count++;
  return n;
}

const map1 = list.map(multFactor);
console.log(map1);
