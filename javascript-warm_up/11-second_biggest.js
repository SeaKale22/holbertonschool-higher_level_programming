#!/usr/bin/node

const numOfArgs = process.argv.length;
let largest = Number.MIN_SAFE_INTEGER;
let secondLargest = Number.MIN_SAFE_INTEGER;

if (numOfArgs <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < numOfArgs; i++) {
    const currentNum = parseInt(process.argv[i]);

    if (currentNum > largest) {
      secondLargest = largest;
      largest = currentNum;
    } else if (currentNum > secondLargest && currentNum < largest) {
      secondLargest = currentNum;
    }
  }
  console.log(secondLargest);
}
