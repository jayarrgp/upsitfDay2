#!/usr/bin/python

"""
HW#3: String Manipulation
Goal: Applying some built in functions for string manipulation
You may find this link helpful: https://www.tutorialspoint.com/python/python_strings.htm
Try if you could use replace method
Programming for Fun. You went back to your childhood years using a time machine invented
by an awesome scientist. You saw your crush and you still could recall his/her complete name.
You decided to create a program using the computer having JDK installed in your time machine.
You wanted to calculate the FLAMES between you and your crush. In this problem, you will
program how FLAMES works. It should take two command-line inputs, your name and your
crush’s name and then should output whether the relationship is F-friendship, L-love,
A-affection, M-marriage, E-enemy and S-soulmate.
For example, the input “William Bradley Pitt” “Angelina Jolie Voight”
Cross out all the letters similar between the two names.
Count the number of all uncrossed out letters.
Determine which among the FLAMES relationships the number falls in.

William Bradley Pitt
Angelina Jolie Voight
F L A M E S F L A M E S F L A M
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Output: Marriage
Another input: “Beverly Reese” “Liam Beesely”
Beverly Reese
Liam Beesely Jr.
F L A M E S
1 2 3 4 5 6
Output: Enemy
Note: Names can contain dot(‘.’). When processing it, it should be excluded in your
computation.
"""

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
