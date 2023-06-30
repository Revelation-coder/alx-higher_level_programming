#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    content = response.read()

    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(content.decode('utf-8')))
