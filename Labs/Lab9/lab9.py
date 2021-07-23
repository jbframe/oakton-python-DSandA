print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/10/2021
Lab # & Name: 9 - Stacks and The Writer's Block
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")

# # write data to a file
# try :
#     f = open("data.txt", "w", encoding = "utf-8")
#     # perform file operations
#     # first line
#     f.write("the first line\n")
#     # second line
#     f.write("the second line\n")
#     # third line
#     f.write("the third line\n")
# finally :
#     f.close()

# # read data from a file
# try :
#     data = []
#     f = open("data.csv", "r", encoding = "utf-8")
#     content = f.read().splitlines()
#     # perform file operations
#     for line in content :
#         print (line)
#         data.append(line)
#         print (data)
# finally :
#     f.close()
#     print (data)

import random
# randomly select an item within a list of elements
myList1 = ["me", "you", "him", "her", "it"]
print (random.choice(myList1))
print ("\n")
# convert a list into a set ( to remove any duplicates )
myList2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
mySet1 = set(myList2)
print (mySet1)
print ("\n")
print (sorted(mySet1))
print ("\n")
# randomly select a subset of elements
samples = random.sample(mySet1, 6)
print (samples)
# sort the subset
sortedList = sorted(samples)
print ("\n")
print (sortedList)
print ("\n\n")

 # list implementation of a Stack
myStack = []
for item in (10, 20, 30, 40) :
    myStack.append(item)
print("The elements in the stack.")
print(myStack)
print ("note: stack treated as a list")
print (type(myStack))
# elements that are popped
# # can be tracked by printing them
print("\nthe elements that were popped are:")
print (myStack.pop())
print (myStack.pop())
print ("\nThe Stack after the elements are popped.")
print (myStack)


