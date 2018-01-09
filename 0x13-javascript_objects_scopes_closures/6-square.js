#!/usr/bin/node

const SquareOld = require('./5-square');

class Square extends SquareOld {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

const s = Square;
module.exports = s;
