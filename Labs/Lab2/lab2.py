print("""
Name: John Frame, Student Number: B02291550, Date: 6/19/2021
Lab Number: 2, Course: CSC 242 Python Data Structures
""")
# ---------------------------------------------------
# define and initialize variables
custID = 0
custName = ""
custAddress = ""
custKilowattHoursUsed = 0.0
custAmountPastDue = 0.0
custTotalAmountDue = 0.0
custPenaltyCharge = 0.0
custSurcharge = 0.0

# ---------------------------------------------------
# helper function to gather customer data
def getCustomerData() :
  global custID, custName, custAddress, custKilowattHoursUsed, custAmountPastDue
  custName = input("Please enter the Customer Name: ")
  custID = input("Please enter the Customer Number: ")
  custAddress = input("Please enter the Customer Address: ")
  custKilowattHoursUsed = float(input("Please enter the Kilowatt-Hours (KWH) used: "))
  custAmountPastDue = float(input("Please enter the amount past due: "))

# ---------------------------------------------------
# helper function to calculate customer bill
def calculateElecticBill() :
  # define and initialize variables
  global custKilowattHoursUsed, custAmountPastDue, custPenaltyCharge, custSurcharge
  penaltyCharge = 0.0; currentCharge = 0.0
  amt = currentCharge + custAmountPastDue + custPenaltyCharge + custSurcharge
  # define the rates and charges
  penaltyPcentage = 2.5
  electricityVariableRates = [0.1, 0.09, 0.08, 0.06]
  electricityBaseCosts = [0, 12.50, 30.60, 42.60]
  electricityBrackets = [0, 125, 320, 500]
  variableKWH = 0.0
  # calculate current charge
  if electricityBrackets[0] < custKilowattHoursUsed <= electricityBrackets[1]:
    variableKWH = custKilowattHoursUsed - electricityBrackets[0]
    currentCharge = variableKWH * electricityVariableRates[0] + electricityBaseCosts[0]

  elif electricityBrackets[1] < custKilowattHoursUsed <= electricityBrackets[2]:
    variableKWH = custKilowattHoursUsed - electricityBrackets[1]
    currentCharge = variableKWH * electricityVariableRates[1] + electricityBaseCosts[1]

  elif electricityBrackets[2] < custKilowattHoursUsed <= electricityBrackets[3]:
    variableKWH = custKilowattHoursUsed - electricityBrackets[2]
    currentCharge = variableKWH * electricityVariableRates[2] + electricityBaseCosts[2]

  else:
    variableKWH = custKilowattHoursUsed - electricityBrackets[2]
    currentCharge = variableKWH * electricityVariableRates[2] + electricityBaseCosts[2]

  # calculate penalty
  custPenaltyCharge = custAmountPastDue * penaltyPcentage / 100

  # calculate surcharge
  if currentCharge > 300:
    custSurcharge = currentCharge * 12 / 100

  # calculate total amount
  amt = currentCharge + custAmountPastDue + custPenaltyCharge + custSurcharge
  return amt


# ---------------------------------------------------
print ()
# call the functions
getCustomerData()
custTotalAmountDue = calculateElecticBill()

# ---------------------------------------------------
# display the Electricity Bill Summary
print ("\nElectricity Bill\n")
print ("\n****************\n")
print ("Customer ID Number\t", custID)
print ("Customer Name\t", custName)
print ("Customer Address\t", custAddress)
print ("Amount Past Due\t", format(custAmountPastDue, "0.2f"))
print ("Penalty\t", format(custPenaltyCharge, "0.2f"))
print ("Surcharge\t", format(custSurcharge, "0.2f"))
print ("Total Amount Due\t", format(custTotalAmountDue, "0.2f"))
print ("\n****************\n")