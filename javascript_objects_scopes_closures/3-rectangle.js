#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let widthLine = '';
    for (let i = 0; i < this.width; i++) {
      widthLine = widthLine + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(widthLine);
    }
  }
}

module.exports = Rectangle;
