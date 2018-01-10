#!/usr/bin/node

const { dict } = require('./101-data');
let a = {};
let v = [];
let temp = [];
let key = 0;

for (key in dict) {
  temp = [];
  v = dict[key];
  if (a[v]) {
    temp = [];
    a[v].forEach(function (element) {
      temp.push(element);
    });
    temp.push(key);
    a[dict[key]] = temp;
  } else {
    temp.push(key);
    a[v] = temp;
  }
}
console.log(a);
