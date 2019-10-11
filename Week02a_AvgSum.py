#!/usr/bin/env python
'''
Created on Feb 7, 2019

@author: noizebot
'''




#input
numOfStudents = int(input("How many students do you have? "))

studentScores= int(input("How many test scores per student? "))

#processing
for student in range(numOfStudents):
    total=0.0
    print("Student number", student+1)  #add 1 to index
    print("-------------")
    for testNum in range(studentScores):
        print("Test number", testNum+1, end= ' ')
        score= float(input(":"))
        total= total + score
    avg=total/studentScores
    print("The average for student number", student+1, "is", format(avg, '.1f'))
    print()
        
        
''' output
How many studens do you have __
How many test scores per student?___

student number 1
------------------

Test Number 1: 
Test Number 2:
Test Number 3:

The average for student number 1 is 

student number 2
-----------------

Test Number 1:
Test Number 2:
Test Number 3:

The average for student number 2 is 

'''