#!/usr/bin/python
"""The aliens invaded the Earth. Their language goes like this: if the letter is a consonant, they spell it as consonant + o + consonant (as in, h = hoh). Vowels are spelled as is. Translate a given list of strings to this alien language using the method map()."""



inputString = input("Enter a string: ").lower()

translatedString = ""
for c in inputString:
	if c not in ('a','e','i','o','u',' '):
		translatedString += c + 'o' + c
	else:
		translatedString += c
print (translatedString)
