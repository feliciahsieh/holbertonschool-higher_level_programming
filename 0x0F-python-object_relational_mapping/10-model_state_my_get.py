#!/usr/bin/python3
"""
Print State object with user input for  name from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    exists = session.query(exists().where(
        State.name.contains(sys.argv[4]))).scalar()
    if (exists):
        for instance in session.query(State).filter(
                State.name.contains(sys.argv[4])).order_by(State.id):
            print("{}".format(instance.id))
    else:
        print("Not found")
