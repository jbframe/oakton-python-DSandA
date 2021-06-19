# EOQ ( Economic Order Quantity )
# The formula for the calculation of an Economic Order Quantity is given as:

#   Q  =  √ [ 2 D S  / H  ]

# where 	Q  is the EOQ units
#   D  is the demand in units ( typically on an annual basis )
#   S  is the order cost ( per purchase order )
#   H  is the holding costs ( per unit, per year )

# Information regarding an EOQ is available at this Web link.
# https://www.investopedia.com/terms/e/economicorderquantity.asp
# Construct a program that will require user input to compute an Economic Order 	Quantity.
# You can test your program with the EOQ example given within the above Web 	link or even the link below.
# https://www.zoho.com/us/inventory/economic-order-quantity/
import math
def calculateEOQ():
  print("\n", "Using the formula Q  =  √ [ 2 D S  / H  ] this program calculates Economic Order Quantity (Q)", "\n")
  d = float(input("Please input D; the demand in units (typically on an annual basis):"))
  s = float(input("Please input S; the order cost (per purchase order):"))
  h = float(input("Please input H; the holding costs (per unit, per year):"))
  d = round(math.sqrt(2 * d * s / h), 3)
  print("\n", "Your Economic Order Quantity (Q) is", d, "\n")
calculateEOQ()