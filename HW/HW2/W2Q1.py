	# Triangular numbers are defined by the infinite set { 1 , 3 , 6 , 10 , 15 , . . . } .

	# Information about triangular numbers can be found at this Web link.

	# https://www.mathsisfun.com/definitions/triangular-number.html

	# The formula to generate the n th Triangular Number is given by this integer 	formula, where n  =  1 , 2 , 3 , 4 , . . .

	# 	T ( n  )  =  ( n 2  +  n  ) / 2

	# Use this formula in the code below to generate the first ten Triangular Numbers.



# define a list
triangleNums = []

# populate the list
for n in range(1, 11):
  triangleNums.append((n**2 + n) / 2)

# display the list elements
print (triangleNums)