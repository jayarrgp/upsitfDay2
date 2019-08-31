#!/usr/bin/python

"""The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet acrophonically so that critical combinations of letters can be pronounced and understood by those who transmit and receive voice messages by radio or telephone regardless of their native language, especially when the safety of navigation or person is essential. 
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',      'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',      'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',      'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',      'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',      'z':'zulu'}
Write a procedure speak_ICAO() that translates any text into spoken ICAO words. Import two libraries: os and time. You have access to the system TTS (text-to-speech) by os.system(‘say ‘ + msg) where msg is the string to be spoken. Aside from the string parameter, accept two floats that will indicate the length of pause between ICAO words (the letters) and between each word spoken."""

import os
import time

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',      'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',      'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',      'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',      'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',      'z':'zulu'}

inputString = input("Enter string : ")
waitTime = float(input("Enter wait time: "))
for c in inputString:
	if c in d:
			print(c,": ",d[c])
	else:
		print (c)
	time.sleep(waitTime)
