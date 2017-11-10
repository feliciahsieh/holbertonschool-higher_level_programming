#!/usr/bin/python3
"""
    file: 2-my_filter_states.py
"""
import MySQLdb


class MyStates:
        """
        mysql table states
        """

        def printMatchingStates(*arg):
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

                t = arg[4]
                cur.execute(
                        "SELECT * FROM states WHERE name=(%s) \
ORDER BY id ASC", (t,))
                rows = cur.fetchall()
                for row in rows:
                        print(row)

                cur.close()
                db.close()

if __name__ == "__main__":
    from sys import argv

MyStates.printMatchingStates(*argv)
