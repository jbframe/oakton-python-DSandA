# Name: John Frame
# Student Number: B02291550
# Date: 6/16/2021
# Lab Number: 4
# Course: CSC 242 Python Data Structures
# ---------------------------------------------------#

# cryptography ( shuffle elements in a list )
# for random shuffle
import random
# for press any key prompt using system commands(MAC OS / Linux)
import os

# the plaintext secret message
printMsg = "Plaintext secret message:"
pageBreak = "---------------------------------------------------"
strMsg = "The Courier is En Route with the Documents"
print(pageBreak); print(printMsg, "\n"); print(strMsg, "\n"); print(pageBreak)

# convert the plaintext to lower case
printMsg = "Lowercase secret message:"
strMsg = strMsg.lower()
print(printMsg, "\n"); print(strMsg, "\n"); print(pageBreak)

# replace any spaces in the message with an "x"
printMsg = "Spaces in the secret message replaced with an 'x':"
strMsg = strMsg.replace(" ", "x")
print(printMsg, "\n"); print(strMsg, "\n"); print(pageBreak)

# declare a one - dimensional list
# populate the list with the characters comprising the message
printMsg = "List with characters comprising of the secrete message:"
plainTxtList = []
# append the characters
for char in strMsg:
    plainTxtList.append(char)
print(printMsg, "\n"); print(plainTxtList, "\n"); print(pageBreak)

# declare the cipher list
scrambledList = []
# use list() to cast the plaintext list into the ciphertext list
scrambledList = list(plainTxtList)
# randomly scramble the list of characters
printMsg = "Shuffled list with characters comprising of the secrete message:"
random.shuffle(scrambledList)
print(printMsg, "\n"); print(scrambledList, "\n"); print(pageBreak)
# determine the length of the list
printMsg = "Length of the scrambled list:"
print(printMsg, len(scrambledList), "\n"); print(pageBreak)

# print in blocks of seven letters per row
printMsg = "Cipher Text:"
print(printMsg, "\n")
cipherTextLine = ""
cipherTextList = []
for index in range(len(scrambledList)):
    cipherTextLine += scrambledList.pop(0)
    if len(cipherTextLine) == 7:
      print(cipherTextLine)
      cipherTextList.append(cipherTextLine)
      cipherTextLine = ""
print(pageBreak)

# ask the user to press any key to continue
os.system('read -s -n 1 -p "Press any key to continue..."')
print()

# attempt to decipher the encrypted message
wordCount = 1

for line in cipherTextList:
  wordCount += line.count('x')
  line = line.replace("x", " ")
  print(line)
print(wordCount)

print(cipherTextList)