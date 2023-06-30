#!/bin/bash
# Script to send a JSON POST request with file contents
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
