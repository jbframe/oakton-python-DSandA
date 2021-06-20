print("""
Name: John Frame, Student Number: B02291550, Date: 6/19/2021
Lab Number: 2, Course: CSC 242 Python Data Structures
""")
# ---------------------------------------------------#
# Babylonian Method
# Programmer: Sammy Student
def Babylonian(number) :
x = number
# (1) choose y = 1 as an initial estimate of square root(x)
# (2) if x > 2 , let y = x / 2
while (True):
# (3) let y = the average of y and x / y
# (4) if y ^ 2 is not close enough to x , then repeat step (3)
# (5) return y , as the square root of x
return y
print ("----- The Babylonian Method -----\n")
radicand = float(input("please enter a positive real number "))
radical = Babylonian(radicand)
print ("the square root of", radicand, "is", radical)