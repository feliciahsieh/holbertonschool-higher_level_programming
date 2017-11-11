#!/usr/bin/python3
"""
model_city.py to create a City object that inherits from Base
links to the MySQL table cities
class attribute id=auto-generated, unique integer, can’t be null, primary key
class attribute name=string of 128 characters and can’t be null
class attribute state_id=integer, can’t be null, foreign key to states.id
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Create a City object that inherits from Base
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
