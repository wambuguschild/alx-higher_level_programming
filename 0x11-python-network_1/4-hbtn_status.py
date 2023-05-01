#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response.raise_for_status()
    content = response.test

    print('Body response:')
    print(f\'t- type: {type(content)}')
    print(f\'t- content: {content}')
