#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('An erroe occured while making the request:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
