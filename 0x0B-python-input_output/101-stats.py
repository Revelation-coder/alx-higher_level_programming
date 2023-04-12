#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""


import sys
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
count = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        words = line.split()
        if len(words) >= 2:
            if words[-2] in status_codes:
                status_codes[words[-2]] += 1
                file_size += int(words[-1])
                count += 1
    if count == 10:
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))
            count = 0
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))
