#!/usr/bin/python3
""" 5-hbtn_header.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    if len(sys.argv) == 2:
        url = sys.argv[1]
        r = requests.get(url)
        print("{}".format(r.headers['X-Request-Id']))
