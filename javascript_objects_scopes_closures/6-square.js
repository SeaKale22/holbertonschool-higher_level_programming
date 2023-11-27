#!/usr/bin/node

// import old square
const oldSquare = require('./5-square');

class Square extends oldSquare {
  // represents a square
  charPrint (c) {
    // pritns the rectangle with a specific character
    let charToPrint = 'X';
    if (c !== undefined) {
      // checks if character was defined
      charToPrint = c;
    }
    let printLine = ''; // define string to hold width characters
    for (let i = 0; i < this.width; i++) {
      // initilize sting with width number of characters
      printLine = printLine + charToPrint;
    }
    for (let j = 0; j < this.height; j++) {
      // print the printLine height number of times
      console.log(printLine);
    }
  }
}

module.exports = Square;
