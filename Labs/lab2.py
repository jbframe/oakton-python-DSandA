# Name: John Frame
# Student Number: B02291550
# Date: 6/16/2021
# Lab Number: 2
# Course: CSC 242 Python Data Structures
# ---------------------------------------------------#
custID = 0
custName = ""

# ---------------------------------------------------
def getCustomerData() :
global custID, custName
custName = input("please enter the Customer Name: ")
custID = int(input("please enter the Customer Number: "))
print (custID)

# ---------------------------------------------------
def calculateElecticBill() :
amt = 0
# place if - elif - else block here
return amt

# ---------------------------------------------------
print ()
# call the functions
getCustomerData()
calculateElecticBill()

# ---------------------------------------------------
# display the Electricity Bill Summary
print ("\nElectricity Bill\n")
print ("\n****************\n")
print ("Customer ID Number\t", custID)
print ("Customer Name\t", custName)