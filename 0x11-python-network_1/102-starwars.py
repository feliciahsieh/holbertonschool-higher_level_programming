#!/usr/bin/python3
""" 102-starwars.py Queries Star Trek database with user string and
prints out character name and movie listing of appearances """
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

    prevPage = ""
    currPage = query
    while prevPage != currPage and currPage is not None:
        r = requests.get(query)
        d = r.json()
        count = 0
        for i in d['results']:
            print(i['name'])
            resu = d['results']
            queryFilm = resu[count]['films']
            for k in range(len(queryFilm)):
                fq = requests.get(queryFilm[k])
                df = fq.json()
                print("\t{}".format(df['title']))
            count += 1
        prevPage = currPage
        currPage = query = d['next']
