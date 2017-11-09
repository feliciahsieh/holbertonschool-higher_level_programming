#!/usr/bin/python3
"""
    define 0-select_states.py
"""
import MySQLdb
import sqlalchemy

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "hbtn_0e_0_usa"))
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(states).all():
    print("{}: {}".format(state.id, state.name))
session.close()
