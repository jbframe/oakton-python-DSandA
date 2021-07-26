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
numbeOfLines = 0
samples = random.sample(grid, 6)
print (samples, grid)
print ("[ the script ]")
print("")
print ("I started the day by looking for the", samples.pop(), end = ".")
numbeOfLines += 1
print ()
print ("I planned later to walk to the", samples.pop(), end = ".")
numbeOfLines += 1
print ()
print ("Surprisingly, I found the", samples.pop(), "was empty", end = ".")
numbeOfLines += 1
print ()
print ("I wondered if a", samples.pop(), "would appear", end = ".")
numbeOfLines += 1
print ()
print ("My aunt must have left my cellular telephone with the", samples.pop(), end = ".")
numbeOfLines += 1
print ()
print ("Yesterday, I forgot to take the", samples.pop(), "to the meeting", end = ".")
numbeOfLines += 1
print ("\n\n")

total_entropy = 0


print ("\n")
print ("please enter an integer 0-5 that will describe the entropy analysis")
for i in range(1, numbeOfLines + 1):
    print ("for grid line " + str(i) + ":")
    entropy = int(input())
    total_entropy += entropy
    print ("estimated entropy for grid line " + str(i) + ":", entropy)
print ("total entropy :",  total_entropy)
print ("\n\n")