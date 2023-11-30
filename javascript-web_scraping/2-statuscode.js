#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

function requestCallback (err, response, body) {
  const statusString = 'code: ' + response.statusCode;
  if (err) {
    // do nothing
  }
  console.log(statusString);
}

request(url, requestCallback);
