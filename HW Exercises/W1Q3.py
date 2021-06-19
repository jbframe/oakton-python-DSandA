#Determine the output of this program when the user inputs the ordered pairs ( 1 , 3 ) and ( 4 , 5 ) .

import math

print ("(x , y) coordinates for point P : ")
x1 = float(input())
y1 = float(input())
print ("(x , y) coordinates for point Q : ")
x2 = float(input())
y2 = float(input())

x_diff_sq = (x2 - x1)**2.0
y_diff_sq = (y2 - y1)**2.0

d = math.sqrt(x_diff_sq + y_diff_sq)
print ("distance between P and Q : ", format(d, "0.2f"))
# output: ?

# (x , y) coordinates for point P :
# 1
# 3
# (x , y) coordinates for point Q :
# 4
# 5
# distance between P and Q :  3.61
