#!/usr/bin/python3
""" 3-error_code.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print("Index")
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(response.getcode()))
