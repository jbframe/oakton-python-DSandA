count = 0
def permutation(list, start, end):
    # function to display all permutations of a given list
    global count
    count = count + 1
    print(count, start, end)
    if (start == end) :
        print (list, count, start, end)
    else :
        for i in range(start, end + 1) :
            list[start], list[i] = list[i], list[start]
            permutation(list, start + 1, end)
            list[start], list[i] = list[i], list[start]

testList = [4, 5, 6, 7]
permutation(testList, 0, 3)
