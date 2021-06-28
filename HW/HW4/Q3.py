import array as myArr
number = myArr.array("b", [2, 3, 5, 4, 3, 3, 3])
numberToCheck = int(input("What number would you like to check occurrences for? "))
print(number.count(numberToCheck))