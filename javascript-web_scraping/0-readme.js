#!/usr/bin/node

// reads and prints the content of a file

const fs = require('fs'); // import fs module

function callBack(err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data)
    }
}

fs.readFile(process.argv[2], 'utf-8', callBack);