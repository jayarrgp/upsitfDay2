#!/usr/bin/python
"""[Do exercise 10 but using class Rectangle]"""

class Rectangle:
	def __init__(self, x, y):
		self.width = x
		self.length = y
	def area(self):
		return self.width*self.length
inputWidth = float(input("Please input width: "))
inputLength = float(input("Please input length: "))
newRectangle = Rectangle(inputWidth, inputLength)
print("Area = ",round(newRectangle.area(),2))
