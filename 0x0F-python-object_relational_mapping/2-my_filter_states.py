#!/usr/bin/python3
"""
    file: 2-my_filter_states.py
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 5:
        exit(0)

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
        cur = db.cursor()

        t = argv[4]
        cur.execute("SELECT * FROM states WHERE name=(%s) \
        ORDER BY id ASC", (t,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except:
        pass
