#!/usr/bin/node

// writes to a file

const fs = require('fs');

const filePath = process.argv[2];
const writeData = process.argv[3];

function writeError (err) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(filePath, writeData, 'utf-8', writeError);
