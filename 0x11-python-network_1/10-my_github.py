#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to display your GitHub ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./10-my_github.py username password")

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/Revelation-coder'

    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        if 'id' in data:
            print(data['id'])
        else:
            print("None")
    except ValueError:
        print("Invalid response from GitHub API")
