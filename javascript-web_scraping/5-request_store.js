#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const requestUrl = process.argv[2];
const filePath = process.argv[3];

function writeError (err) {
  if (err) {
    console.log(err);
  }
}

function requestCallback (err, response, body) {
  if (err) {
    // do nothing
  }
  fs.writeFile(filePath, body, 'utf-8', writeError);
}

request(requestUrl, requestCallback);
