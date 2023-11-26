#!/usr/bin/node

const message = 'C is fun';
const numOfMessage = parseInt(process.argv[2]);

if (isNaN(numOfMessage)) {
  console.log('Missing number of occurrences');
}
if (!isNaN(numOfMessage)) {
  for (let i = 0; i < numOfMessage; i++) {
    console.log(message);
  }
}
