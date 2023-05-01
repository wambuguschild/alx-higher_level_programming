#!/usr/bin/pythom3
""" A script that takes in a URL and an email address sends a POST request
and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
