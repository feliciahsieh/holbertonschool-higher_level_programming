#!/usr/bin/python3
"""
Print all State objects that contain the letter a from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for i, instance in enumerate(session.query(State).
                                 filter(State.name.contains('a')).
                                 order_by(State.id)):
        print("{}: {}".format(i, instance.name))
