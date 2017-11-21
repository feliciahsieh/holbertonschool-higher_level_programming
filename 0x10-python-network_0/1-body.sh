#!/bin/bash
# Send a GET request to URL and display body of the response
curl -sw "%{http_code}" 0.0.0.0:5000/route_1
