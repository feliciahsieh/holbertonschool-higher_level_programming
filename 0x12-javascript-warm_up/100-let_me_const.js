#!/usr/bin/node
var q = function () {};

q.prototype.log = function () {
  console.log('333');
};

exports.q = new q();
