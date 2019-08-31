#!/usr/bin/python
"""	Create a class Circle with methods __init__(self, r) where r is the radius of the circle, and area(self) which is the area of the circle. Make sure you also create an attribute radius, which is equal to the value of r. The user will input the desired radius, and your program should compute the area. """
from math import *

class Circle:
	def __init__(self, r):
		self.radius = r
	def area(self):
		return self.radius**2*pi
inputR = float(input("Please input desired radius: "))
NewCircle = Circle(inputR)
print("Area = ",round(NewCircle.area(),2))
