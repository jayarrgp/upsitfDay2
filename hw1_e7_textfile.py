#!/usr/bin/python
"""Given an input text file, create a new file that numbers the input text file per line. Use the argv module from the sys package so that your run command is something like: python exercise6.py input.txt output.txt"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv
input = open(from_file)
indata = input.read()
if not exists(to_file):
	with open(to_file, 'a') as output:
		for i in range(len(from_file)):
			i+=1
			output.write(str(i) + "\n")
		output.close()
input.close()
