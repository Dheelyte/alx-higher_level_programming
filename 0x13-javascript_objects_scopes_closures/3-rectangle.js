#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i, j;
    let string = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        if (j === this.width - 1 && i !== this.height - 1) {
          string += 'X\n';
        } else {
          string += 'X';
        }
      }
    }
    console.log(string);
  }
}
module.exports = Rectangle;
