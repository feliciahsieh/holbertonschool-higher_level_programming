#!/usr/bin/python3
"""
    file: 0-select_states.py
"""
import MySQLdb


class MyStates:
        """
        mysql table states
        """

        def printStates(*arg):
                """
                Display all states in mySQL table, states
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

                cur.execute("SELECT * FROM states ORDER BY id ASC")
                rows = cur.fetchall()
                for row in rows:
                        print(row)

                cur.close()
                db.close()

if __name__ == "__main__":
    from sys import argv

MyStates.printStates(*argv)
