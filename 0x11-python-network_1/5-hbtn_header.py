#!/usr/bin/python3
""" 5-hbtn_header.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)
    print("{}".format(r.headers['X-Request-Id']))
