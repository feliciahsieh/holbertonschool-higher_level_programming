#!/bin/bash
# Display all HTTP methods server will accept for user's URL
curl -sIX OPTIONS 0.0.0.0:5000/route_4 | awk -F': ' '/Allow/ { print $2 }'
