print("""
--------------------------------Remarks------------------------------------
Programmer: John Frame, Student Number: B02291550, Date: 6/21/2021
Lab # & Name: 3 - Babylonian Method, Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")
# ------------------------------------------------------------------------#
def Babylonian(number):
  x = number
  # (1) choose y = 1 as an initial estimate of square root(x)
  y = 1.0
# ------------------------------------------------------------------------#
  # create and initialize variables
  # Store the square of y
  ySquared = 0.0
  iterationCounter = 1
# ------------------------------------------------------------------------#
  # (2) if x > 2 , let y = x / 2
  if x > 2:
    y = x / 2
  # specify the accuracy
  e = 10**-9
  print('iteration number', '\tapproximation')
  while (True):
    # (3) let y = the average of y and x / y
    y = (y + x / y) / 2
    # (4) if y ^ 2 is not close enough to x , then repeat step (3)
    ySquared = y**2
    print(iterationCounter, '\t\t\t', round(y,7))
    iterationCounter += 1
    if ySquared - x < e:
    # (5) return y , as the square root of x
      return y
print ("----- The Babylonian Method -----\n")
radicand = float(input("please enter a positive real number "))
radical = Babylonian(radicand)
print ("\n", "the square root of", radicand, "is", radical, "\n")