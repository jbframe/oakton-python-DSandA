# ( Lists: Squaring the Odd Numbers )

# Modify the program segment below such that not only the list elements are displayed but also the length of the list.

# define a list
oddSquares = []
# populate the list
for x in range(1, 11):
		if (x % 2 == 1) :
				oddSquares.append(x**2)
# display the list contents
print(f"""
{oddSquares} \tLength of odd squares list: {len(oddSquares)}
""")