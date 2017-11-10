#!/usr/bin/python3
"""
    file: 4-cities_by_state.py
"""
import MySQLdb


class MyStates:
        """
        mysql table states
        """

        def printCities(*arg):
                """
                Display all states that match user input in mySQL table, states
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

                cur.execute(
                        "SELECT cities.id, cities.name, states.name \
FROM cities \
INNER JOIN states ON cities.state_id \
WHERE cities.state_id=states.id \
ORDER BY cities.id ASC")
                rows = cur.fetchall()
                for row in rows:
                        print(row)

                cur.close()
                db.close()

if __name__ == "__main__":
    from sys import argv

MyStates.printCities(*argv)
