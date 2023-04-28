#!/bin/bash
# A script that displays size of the HTTP response body of a URL
curl -s "$1" | wc -c
