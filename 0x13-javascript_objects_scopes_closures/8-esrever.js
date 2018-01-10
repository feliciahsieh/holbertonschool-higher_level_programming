#!/usr/bin/node

module.exports.esrever = function (list) {
  let l = list.length;
  let revList = [];
  list.forEach(function (entry) {
    revList[--l] = entry;
  });
  return revList;
};
