#!/usr/bin/python3
""" 1-hbtn_header.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print("{}".format(headers['X-Request-Id']))
