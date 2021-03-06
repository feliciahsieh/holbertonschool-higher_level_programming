#!/usr/bin/python3
""" 0-hbtn_status.py """
if __name__ == "__main__":
    """ __main__ """
    import urllib.request as request


    url = 'https://intranet.hbtn.io/status/'
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
