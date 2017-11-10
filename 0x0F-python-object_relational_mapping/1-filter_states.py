#!/usr/bin/python3
"""
    file: 1-filter_states.py
"""
import MySQLdb


class MyStates:
        """
        mysql table states
        """

        def print_N_States(*arg):
                """
                Display all states that start with 'N' in mySQL table, states
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
                        "SELECT * FROM states WHERE name LIKE 'N%' \
ORDER BY id ASC")
                rows = cur.fetchall()
                for row in rows:
                        print(row)

                cur.close()
                db.close()

if __name__ == "__main__":
    from sys import argv

MyStates.print_N_States(*argv)
