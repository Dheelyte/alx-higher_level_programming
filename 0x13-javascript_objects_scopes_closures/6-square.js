#!/usr/bin/node

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    let i;
    for (i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
