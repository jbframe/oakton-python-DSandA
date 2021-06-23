print("""
Name: John Frame, Student Number: B02291550, Date: 6/19/2021
Lab # & Name: 4 - cryptography, Course: CSC 242 Python Data Structures
""")
# ---------------------------------------------------#

# cryptography ( shuffle elements in a list )
# for random shuffle
import random
# for press any key prompt using system commands(MAC OS / Linux)
import os
# to time how long burute for decryption takes
import time
# the plaintext secret message
printMsg = "Plaintext secret message:"
pageBreak = "---------------------------------------------------"
strMsg = "The Courier is En Route with the Document"
print(); print(pageBreak); print(printMsg, "\n"); print(strMsg, "\n"); print(pageBreak)

# convert the plaintext to lower case
printMsg = "Lowercase secret message:"
strMsgLowerCase = strMsg.lower()
print(printMsg, "\n"); print(strMsgLowerCase, "\n"); print(pageBreak)

# replace any spaces in the message with an "x"
printMsg = "Spaces in the secret message replaced with an 'x':"
strMsgLowerCaseNoSpaces = strMsgLowerCase.replace(" ", "x")
print(printMsg, "\n"); print(strMsgLowerCaseNoSpaces, "\n"); print(pageBreak)

# declare a one - dimensional list
# populate the list with the characters comprising the message
printMsg = "List with characters comprising of the secrete message:"
plainTxtList = []
# append the characters
for char in strMsgLowerCaseNoSpaces:
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
cipherTextLine = ""
cipherTextList = []
print(printMsg, "\n");
for index in range(len(scrambledList)):
    cipherTextLine += scrambledList.pop(0)
    if len(cipherTextLine) == 7:
      print(cipherTextLine)
      cipherTextList.append(cipherTextLine)
      cipherTextLine = ""
cipherTextList.append(cipherTextLine)
print(cipherTextLine, "\n"); print(pageBreak)
# ask the user to press any key to continue
os.system('read -s -n 1 -p "Press any key to continue..."')
print()

####### attempt to decipher the encrypted message ########
# convert cipher to string and replace x's with spaces
cipherTextString = ""
for line in cipherTextList:
    line = line.replace("x", " ")
    cipherTextString += line
printMsg = "Cipher text string:"
pageBreak = "---------------------------------------------------"
print(pageBreak); print(printMsg, "\n"); print(cipherTextString, "\n"); print(pageBreak)
cipherTextStringShuffle = ''


### DECRYPTION SCHEME IF WE CAN CHECK AFTER GUSSING EACH CHARACTER ##
start = time.perf_counter()
cipherTextStringLength = len(cipherTextString)
charMatched = 0
decryptedMessage = ''
for i in range(cipherTextStringLength):
    for j in range(cipherTextStringLength):
        if strMsgLowerCase[i] == cipherTextString[j]:
            decryptedMessage += cipherTextString[j]
            break
finish = time.perf_counter()
print("You decrypted the message CHARACTER BY CHARACTER:", "\n"); print(decryptedMessage, "\n")
print("in", round(finish-start, 4), ' seconds'); print(pageBreak, "\n")

### DECRYPTION SCHEME TO RANDOMLY GUESS ENTIRE STRING ##
start = time.perf_counter()
while cipherTextStringShuffle != strMsgLowerCase:
    del cipherTextStringShuffle
    cipherTextStringShuffle = ''.join(random.sample(cipherTextString, len(cipherTextString)))
    # print(cipherTextStringShuffle)
finish = time.perf_counter()
print("You RANDOMLY decrypted the message:", "\n"); print(decryptedMessage, "\n")
print("in", round(finish-start, 4), ' seconds'); print(pageBreak, "\n")