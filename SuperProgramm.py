import math


class Figure:
    def __del__(self):
        print ("figure ",self," has been deleted");


class Point(Figure):
    _x=0
    _y=0
    def __init__(self, x, y):
        self._x = x
        self._y = y
        print("the figure ", self," has been crated")

    def set_x(self, x):
        self._x=x
    def set_y(self,y):
        self._y=y

    def get_coordinates(self):
        print ("x=",self._x,"y=",self._y)

    def how_long_if_from_center(self):
        print (   math.sqrt((0-self._x)**2 + (0-self._y)**2)    )

class circle(Point):
    _r=0
    def __init__(self, x, y, r):
        self._r = r
        self._x = x
        self._y = y
        print("the figure ", self," has been created")

    def set_r(self,r):
        self._r=r

    def get_radius(self):
        print ("r=",self._r)

    def get_length(self):
        print ("l=",2*self._r*3.14)






