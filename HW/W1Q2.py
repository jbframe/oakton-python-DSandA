print ("fun with assignment statements")
x = []
y = 3
z = 5
x = y + z
y = x + y
z = x - y + z
print (2 * x + (y + 5) - 3 * z)
# output: 26
# The value assigned to x on line 2 could be anything because x is assigned to a new value on line 5 before it is used in any expressions.