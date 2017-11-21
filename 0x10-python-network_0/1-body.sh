#!/bin/bash
# Send a GET request to URL and display body of the response
curl -sw "%{http_code}" $1
