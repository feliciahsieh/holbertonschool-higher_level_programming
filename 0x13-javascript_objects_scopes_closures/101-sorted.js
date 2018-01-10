#!/usr/bin/node

const { dict } = require('./101-data');
console.log(dict);

let a = {};
let l = [];
let i = 0;
//object.keys(obj)
for(key in dict) {
  l = a[dict[key]];
  console.log(l);
  a[dict[key]] = key;
}
  


console.log(a);
