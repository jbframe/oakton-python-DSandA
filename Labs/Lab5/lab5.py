# menu selector
select = 0

def DisplayMenu() :
    print ("enter your choice")
    print ("1 for a Linear Search")
    print ("2 for a Binary Search")
    print ("3 for a Bubble Sort")
    print ("4 for a Selection Sort")
    print ("5 for a Insertion Sort")

def SelectRoutine() :
    global select

    DisplayMenu()
    select = int(input())
    if (select == 1) :
        print ("Call the Linear Search Routine")
        LinearSearch()
    elif (select == 2) :
        print ("Call the Binary Search Routine")
    else :
        print("invalid selection")

SelectRoutine()


# search a list for particular elements

# declare a list of letters and numbers
myList = ["A", "B", "C", "D", 1, 2, 3]
# locate an item within the list
findIt = myList.index("C")
print (findIt) # returns the index 2
# do not locate an item within the list
doNotFindIt = "E"
check1 = doNotFindIt not in myList
print (check1) # returns True

# search a list for some particular elements
if ("B" in myList) :
    print ("item was located")
if ("1" in myList) :
    print ("item was located")
else :
    print ("item was NOT located")


# implementation of a Linear Search

# time complexity ( Order of Magnitude ) : O(n)

elements = [10, 20, 80, 70, 60, 50]

x = int(input("please enter the number to search: "))

# Boolean Flag
found = False

for i in range(len(elements)) :

    if(elements[i] == x) :
        found = True
        print("%d found at %dth position" % (x, i))
        break
    if (found == False) :
        print("%d is not in list" % x)



def binarySearch(sortedlist, n, x) :
    start = 0
    end = n - 1

    while(start <= end) :
        mid = int((start + end) / 2)
        if (x == sortedlist[mid]) :
            return mid
        elif(x < sortedlist[mid]) :
            end = mid - 1
        else :
             start = mid + 1
    return -1

n = int(input("Enter the size of the list: "))

sortedlist = []

# populate the list in sort entry order
for i in range(n) :
    sortedlist.append(int(input("Enter %dth element: " % i)))

x = int(input("Enter the number to search: "))
position = binarySearch(sortedlist, n, x)

if (position != -1) :
    print("element number %d is present at position: %d" % (x, position))
else :
    print("element number %d is not present in the list" % x)



# program for implementing a Bubble Sort

def bubbleSort(arr) :

    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1) :
    # range(n) also work but outer loop will repeat one time
    # more than necessary

        # Last i elements are already in place
        for j in range(0, n - i - 1) :

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# driver code to test the above routine
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("the sorted array is:")
for i in range(len(arr)) :
    print ("%d" %arr[i]),


# Routine for a Selection Sort

A = ['t','e','s','t','d','a','t','a']

for i in range(len(A)) :
    min_= i
    for j in range(i + 1, len(A)) :
        if (A[min_] > A[j]) :
            min_ = j
    # swap performed
    A[i], A[min_] = A[min_], A[i]

# main
for i in range(len(A)) :
   print (A[i])


