#!/usr/bin/python3
""" 10-my_github.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/users/'
    r = ""
    if len(sys.argv) == 3:
        username = sys.argv[1]
        passw = sys.argv[2]
        url = url + username
        r = requests.get(url, auth=HTTPBasicAuth(username, passw))
    else:
        print("Try again")
        sys.exit(0)

    d = r.json()
    print(d['id'])
