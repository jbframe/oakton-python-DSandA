# Name: John Frame
# Student Number: B02291550
# Date: 6/16/2021
# Lab Number: 1
# Course: CSC 242 Python Data Structures
# ---------------------------------------------------#
print ("Program: Target GPA")
print ("Programmer: Sammy Student")
print ("-------------------------")

# ---------------------------------------------------#
# variables declared and initialized
msg1 = ""; msg2 = ""
totalHours = 0; creditsEarned = 0; creditsCurrent = 0
currentGPA = 0; targetGPA = 0
targetGradePoints = 0; requiredGPA = 0
# ... declare and assign any additional variables here ...

# ---------------------------------------------------#
# print ("----- INPUTING Data -----")
msg1 = "GPA credit hours already completed ( Credits Earned ) "
creditsEarned = int(input("enter " + msg1))
msg2 = "Current GPA ( Cumulative ) "
currentGPA = float(input("enter " + msg2))
# ... complete the input section of this program ...

# ---------------------------------------------------#
print ("----- PROCESSING Data -----")
totalHours = creditsEarned + creditsCurrent
targetGradePoints = targetGPA * totalHours
targetGradePoints -= creditsEarned * currentGPA
# ... complete the processing section of this program ...

# ---------------------------------------------------#
print ("----- OUTPUTTING Data -----")
# ... complete the output section of this program ...
print ("Required GPA", format(requiredGPA, "0.2f"))