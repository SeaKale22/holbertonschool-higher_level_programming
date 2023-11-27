#!/usr/bin/node

// import rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    // represents a square
    constructor (size) {
        super(size, size); // calls constructor of rectangle
    }
}

module.exports = Square;
