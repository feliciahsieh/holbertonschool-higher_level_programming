#!/usr/bin/python3
""" 8-json_api.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        if len(sys.argv[1]) == 1:
            q = sys.argv[1]
            pass
        else:
            print("Not a valid JSON")
    else:
        print("No result")

    r = requests.post(url, q)
