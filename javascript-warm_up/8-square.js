#!/usr/bin/node

const sizeOfSquare = parseInt(process.argv[2]);
let squareLine = '';

if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
}
if (!isNaN(sizeOfSquare)) {
  for (let i = 0; i < sizeOfSquare; i++) {
    squareLine = squareLine + 'x';
  }
  for (let j = 0; j < sizeOfSquare; j++) {
    console.log(squareLine);
  }
}
