#!/usr/bin/python
"""From a file simpsons_phone_book.txt, print all lines that matches these characteristics: starts with J, followed by any letter, and surname is Neu. Some input may be improperly spaced so it should follow that names with several spaces between the first name and last name is accepted."""

from sys import argv
import re

script, from_file = argv
input = open("simpsons_phone_book.txt")
with open(from_file) as input:
	for line in input:
		matches = re.findall(r"J[a-zA-Z].*Neu",line)
		print(matches)
input.close()
