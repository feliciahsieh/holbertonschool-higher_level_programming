#!/usr/bin/node
var q = function (a) {};

q.prototype.log = function () {
  console.log('333');
};

exports.q = new q();
