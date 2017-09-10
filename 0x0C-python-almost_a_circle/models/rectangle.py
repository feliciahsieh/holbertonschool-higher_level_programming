#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def __width(self):
        return self.width

    @__width.setter
    def __width(self, value):
        self.width = value

    @property
    def __height(self):
        return self.height

    @__height.setter
    def __height(self, value):
        self.height = value

    @property
    def __x(self):
        return self.x

    @__x.setter
    def __x(self, value):
        self.x = value

    @property
    def __y(self):
        return self.y

    @__y.setter
    def __y(self, value):
        self.y = value
