# ( Loops and Control Breaks )

# Modify the program code such that the values of variables x , y and z are 	displayed to the user after the loop body is executed.

y = 0
z = 0

for x in range(3, 7):
		if (y > z ) :
				z, y = y, z
	y = y + x
