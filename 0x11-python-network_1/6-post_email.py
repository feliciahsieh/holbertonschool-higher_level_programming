#!/usr/bin/python3
""" 6-post_email.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    url = sys.argv[1]
    email = {}
    email['email'] = sys.argv[2]
    r = requests.post(url, data=email)
    print(r.text)
