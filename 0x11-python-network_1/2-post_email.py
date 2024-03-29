#!/usr/bin/python3
""" A script that sends POST to a given URL with a given email."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode()
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
