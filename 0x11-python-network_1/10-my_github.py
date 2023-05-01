#!usr/bin/python3
""" A script that takes your GitHub credentials and uses the GitHub API to display your ID"""

import sys
import requests
from requests.auth import HTTPSBasicAuth

if __name__ == "__main__":
    auth = HTTPSBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
