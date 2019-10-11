'''
Created on Jan 23, 2019

@author: noizebot
'''

#Student Name
#Student ID
#This program finds the sum and average

#Program to allow user to input the 3 numbers
#Calculate sum and average 

#input
name = input("What is your name? ")   #syntax var = input("string")
num1 = int(input("Enter the first number "))    #syntax var = dataType(input("string"))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))

#Calculate
sum = num1 + num2 + num3            #sum of 3 numbers

avg = sum/3

#output
#argument follows the string statement seperated by a comma
print("Welcome to Python Programming ", name)   
print("Number 1 is ", num1)
print("Number 2 is ", num2)
print("Number 3 is ", num3)
print("The sum is ", sum)
print("The average is ", avg)

#ask the user to quit program
#also acts as a system('pause')
print("\n\nPress enter to quit")


