from os import system
system("clear")

print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/10/2021
Lab # & Name: 9 - Stacks and The Writer's Block
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")
import csv
import random

# the Writer's Grid
grid = []
with open ('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in row:
            grid.append(i)


# randomly select a subset of elements ( the stack )
samples = random.sample(grid, 6)
# print (samples)
print ("[ the script ]")
print("")
print ("I started the day by looking for the", samples.pop(), end = ".")
print ()
print ("I planned later to walk to the", samples.pop(), end = ".")
print ()
print ("Surprisingly, I found the", samples.pop(), "was empty", end = ".")
print ()
print ("I wondered if a", samples.pop(), "would appear", end = ".")
print ()
print ("My aunt must have left my cellular telephone with the", samples.pop(), end = ".")
print ()
print ("Yesterday, I forgot to take the", samples.pop(), "to the meeting", end = ".")
print ("\n\n")

total_entropy = 0
print ("\n")
print ("please enter an integer 0-5 that will describe the entropy analysis")
print ("for grid line 1")
entropy = int(input())
total_entropy += entropy
print ("estimated entropy for grid line 1:", entropy)
print ("for grid line 2")
entropy = int(input())
print ("estimated entropy for grid line 2:",  entropy)
total_entropy += entropy
print ("total entropy :",  total_entropy)
print ("\n\n")
