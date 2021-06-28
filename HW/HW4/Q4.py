import array as arr
grid = [[1, 2, 3, 5, 7, 10], [6, 2, 4, 5, 9, 11]]
sum = 0
for row in range(len(grid)):
    for column in range(len(grid[0])):
        sum += grid[row][column]
print (sum)