#!/usr/bin/python3
""" 8-json_api.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    params = {}
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 2:
        if len(sys.argv[1]) == 1 and sys.argv[1].isalpha():
            params['q'] = sys.argv[1]
        else:
            print("No result")
            sys.exit(0)
    else:
        print('No result')
        sys.exit(0)

    r = requests.post(url, data=params)
    try:
        d = r.json()
        print("[{}] {}".format(d['id'], d['name']))
    except:
        print("Not a valid JSON")
