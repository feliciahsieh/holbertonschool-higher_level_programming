#!/usr/bin/python3
"""
    file: 5-filter_cities.py
"""
import MySQLdb


class MyStates:
        """
        mysql table states
        """

        def printCitiesInState(*arg):
                """
                Display all cities that match user inputted state
                Args:
                    args: arguments being passed in
                """

                db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=arg[1],
                        passwd=arg[2],
                        db=arg[3])
                cur = db.cursor()

                st = arg[4]
                cur.execute(
"SELECT cities.name FROM cities \
WHERE cities.state_id in (SELECT states.id FROM states WHERE states.name='Texas') \
ORDER BY cities.id ASC")
                rows = cur.fetchall()
                for row in rows:
                        print(row)

                cur.close()
                db.close()

if __name__ == "__main__":
    from sys import argv

MyStates.printCitiesInState(*argv)
