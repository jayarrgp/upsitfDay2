#!/usr/bin/python

"""From a string input, create a per-word letter-counter that excludes the article the from the count. Use a shorthand looping in lists."""

inputString = input("Please enter a string: ").lower()
listString = inputString.split()
print(listString)
filterString = list(filter(lambda a: a !='the', listString))
filterString = {c:len(c) for c in filterString}
print(filterString)