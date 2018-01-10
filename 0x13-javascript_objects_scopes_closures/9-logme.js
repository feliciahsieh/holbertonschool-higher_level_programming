#!/usr/bin/node

let count = 0;
module.exports.logMe = function (item) {
  function newCount () {

  }
  newCount();
  console.log(count + ': ' + item);
  count++;
};
