#!/usr/bin/node

const firstArg = process.argv[2];
const convToInt = parseInt(firstArg);

if (isNaN(convToInt)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + convToInt);
}
