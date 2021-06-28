import array as myArr
# array concatenation
first = myArr.array("u", [u'\u004A', u'\u006F', u'\u0068', u'\u006E'])
second = myArr.array("u", [u'\u0046', u'\u0072', u'\u0061', u'\u006D', u'\u0065'])
fullName = myArr.array("u")
fullName = first + second
print (fullName)
