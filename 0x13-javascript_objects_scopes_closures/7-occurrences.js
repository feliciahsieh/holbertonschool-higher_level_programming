#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (entry) {
    if (entry === searchElement) {
      count++;
    }
  });
  return count;
};
