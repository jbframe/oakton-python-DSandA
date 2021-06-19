print("""
Name: John Frame, Student Number: B02291550, Date: 6/19/2021
Lab Number: 1, Course: CSC 242 Python Data Structures
""")
#---------------------------------------------------#
print ("Program: Target GPA")
print ("Programmer: John Frame")
print ("-------------------------")

# ---------------------------------------------------#
# variables declared and initialized
msg1 = ""; msg2 = ""; msg3 = ""; msg4 = ""
totalHours = 0; creditsEarned = 0; creditsCurrent = 0
currentGPA = 0.0; targetGPA = 0.0
targetGradePoints = 0; requiredGPA = 0
bestPossibleGPA = 0.0

# ---------------------------------------------------#
# print ("----- INPUTING Data -----")
msg1 = "GPA credit hours already completed ( Credits Earned ) "
creditsEarned = int(input("Enter " + msg1))
msg2 = "Current GPA ( Cumulative ) "
currentGPA = float(input("Enter " + msg2))
msg3 = "Credit hours currently enrolled ( Remaining / Planned Credits ) "
creditsCurrent = int(input("Enter " + msg3))
msg4 = "desired Target GPA "
targetGPA = float(input("Enter " + msg4))

# ---------------------------------------------------#
print ("----- PROCESSING Data -----")
totalHours = creditsEarned + creditsCurrent
targetGradePoints = targetGPA * totalHours
targetGradePoints -= creditsEarned * currentGPA
# calculate the required GPA
requiredGPA = targetGradePoints / creditsCurrent
# calculate the best possible GPA
bestPossibleGPA = (4 * creditsCurrent + (creditsEarned * currentGPA)) / totalHours

# ---------------------------------------------------#
print ("----- OUTPUTTING Data -----")
print (f"Required GPA for all remaining {creditsCurrent} credit's:", format(requiredGPA, "0.2f"))
print (f"Best Possible GPA (assuming Straight A's) for all remaining {creditsCurrent} credit's:", format(bestPossibleGPA, "0.3f"), "\n")