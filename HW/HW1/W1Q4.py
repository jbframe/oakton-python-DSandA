# Will these two print() statements display the same result?
# Place your answer in the space provided.

# De Morgan's Logic Principles
x = 0
print (not(x > 3 and x < 10))
print (not(x > 3) or not(x < 10))
# your answer:

# YES!

# not(x > 3 and x < 10)
# = not(False and True)
# = not(False)
# = True

# not(x > 3) or not(x < 10)
# = not(False or not(true))
# = not(False or False)
# = not(False)
# = True

