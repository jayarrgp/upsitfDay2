#!/usr/bin/python

"""HW#3: String Manipulation, Goal: Applying some built in functions for string manipulation""" 

nameMale = input("Enter Male name: ").lower()
nameFemale = input("Enter Female name: ").lower()

uniqueLetMale = [c for c in nameMale if c not in nameFemale if c.isalpha()]
uniqueLetFemale = [c for c in nameFemale if c not in nameMale if c.isalpha()]

flamesCount = len(uniqueLetMale + uniqueLetFemale)

flamesChar = ('FLAMES'*flamesCount)[:flamesCount]
print("\n" + '  '.join([c for c in flamesChar]))
print('  '.join(str(i) for i in range(1,flamesCount+1)) + "\n")

if (flamesCount % 6 == 1):
	print("Output : Friendship")
elif (flamesCount % 6 == 2):
	print("Output : Love")
elif (flamesCount % 6 == 3):
	print("Output : Affection")
elif (flamesCount % 6 == 4):
	print("Output : Marriage")
elif (flamesCount % 6 == 5):
	print("Output : Enemy")
elif (flamesCount % 6 == 0):
	print("Output : Soulmate")