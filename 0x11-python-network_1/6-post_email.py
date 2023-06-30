#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the body of the response.
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}

response = requests.post(url, data=payload)
print("Your email is: {}".format(response.text))
