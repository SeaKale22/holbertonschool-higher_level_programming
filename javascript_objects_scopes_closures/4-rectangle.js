#!/usr/bin/node

class Rectangle {
  // represents a rectangle with various methods
  constructor (w, h) {
    // constructed with width and height
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // prints the rectangle
    let widthLine = '';
    for (let i = 0; i < this.width; i++) {
      widthLine = widthLine + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(widthLine);
    }
  }

  rotate () {
    // extanges width and height
    const newHeight = this.width;
    this.width = this.height;
    this.height = newHeight;
  }

  double () {
    // doubles width and height
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
