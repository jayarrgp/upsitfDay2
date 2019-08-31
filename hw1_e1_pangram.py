#!/usr/bin/python3
"""Identify if a given string is a pangram. A pangram is a sentence, phrase or verse that contains all the letters of the alphabet."""

import string 

alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
  
inputString = input("Please input string : ")

if set(inputString.lower()) >= alphabet:
    print("String is a Pangram") 
else: 
    print("String is a NOT Pangram") 