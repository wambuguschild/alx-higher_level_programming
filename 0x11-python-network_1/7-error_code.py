#!/usr/bin/python3
""" A script that takes in a URL sends a request
and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = request.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
