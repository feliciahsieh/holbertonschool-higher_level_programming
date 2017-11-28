#!/usr/bin/python3
""" 9-starwars.py """
if __name__ == "__main__":
    """ __main__ """
    import sys
    import requests

    url = query = 'https://swapi.co/api/people/?search='
    if len(sys.argv) == 2:
        person = sys.argv[1]
        query = url + person
    else:
        print("No result")

    r = requests.get(query)
    d = r.json()

    print("Number of results: {}".format(d['count']))
    for i in d['results']:
        print(i['name'])
