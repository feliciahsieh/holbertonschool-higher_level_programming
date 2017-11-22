#!/bin/bash
# Send a POST request to User's URL w/2 vars and display the body of the response
curl -sX POST --data "email: hr@holbertonschool.com&subject: I will always be here for PLD" 0.0.0.0:5000/route_6
