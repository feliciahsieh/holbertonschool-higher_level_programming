#!/usr/bin/python3
""" 2-post_email.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        respData = response.read()
        print("{}".format(respData.decode('ascii')))
