#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("    - type: {}".format(type(response.text)))
print("    - content: {}".format(response.text))
