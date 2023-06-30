#!/bin/bash
# Script to send request to a URL and display the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
