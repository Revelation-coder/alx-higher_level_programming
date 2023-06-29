#!/bin/bash
# Script to send request to a URL and display the status code

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo "$response"

