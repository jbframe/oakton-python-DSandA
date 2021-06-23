# ( Loops and Control Breaks )

# 	What is the output of the following code if the if() statement condition was 	negated?

sum = 0
for value in range(1, 4) :
		if (value != 2):
				sum = sum**2
				sum += value
print (f"""
{sum}
""") # expected output: 4