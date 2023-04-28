#!/bin/bash
# A script that takes in a URL as an argument sends a GET request and displays the body of the response
curl -sH "X-school-User-Id: 98" "$1"
