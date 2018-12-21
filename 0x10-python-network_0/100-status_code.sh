#!/bin/bash
# print out HTML status code only from user's URL on command line
curl -o /dev/null -s -w "%{http_code}" "$1"
