#!/usr/bin/python3
""" 2-post_email.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    values = { 'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)

    #with urllib.request.urlopen(url) as response:
    #     query_args = {'email': email}
    #     params = parse.urlencode(query_args)
    #     f = urllib.request.urlopen(url, params)
    #    print("Your email is: {}".format(f.read()))
