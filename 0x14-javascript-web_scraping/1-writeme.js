#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error('An error occured while writing to the file:', err);
  } else {
    console.log('Content has been written to the file successfully.');
  }
});
