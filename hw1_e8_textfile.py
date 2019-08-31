#!/usr/bin/python
"""From an input text file, get the average count of all the letters in that file."""

from sys import argv

script, from_file = argv
input = open(from_file)
indata = input.read()
with open(from_file) as input:
    lines=0
    words=0
    characters=0
    for line in input:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
#print(lines)
#print(words)
#print(characters)
print("Average letters = ", characters/lines)
input.close()
