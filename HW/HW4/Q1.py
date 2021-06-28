import array as arr
numbers = arr.array("u", [u'\u0031',u'\u0032',u'\u0033',u'\u0035',u'\u0037',u'\u0010'])


# change the first element
numbers[0] = u'\u0030'
print (numbers)    # Output: array('i', [0, 2, 3, 5, 7, 10])

# change the 3rd to the 5th element
numbers[2 : 5] = arr.array("u", [u'\u0034',u'\u0036',u'\u0038'])
print (numbers)    # Output: array('i', [0, 2, 4, 6, 8, 10])