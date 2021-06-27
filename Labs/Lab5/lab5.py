print("""
Name: John Frame, Student Number: B02291550, Date: 6/26/2021
Lab # & Name: 5 - Searching and Sorting Techniques with Time Complexity
Course: CSC 242 Python Data Structures
""")

# ----------------Sequential Search (without explicit iterations)------------------- #
# # search a list for particular elements

# # declare a list of letters and numbers
# myList = ["A", "B", "C", "D", 1, 2, 3]
# # locate an item within the list
# findIt = myList.index("C")
# print (findIt) # returns the index 2
# # do not locate an item within the list
# doNotFindIt = "E"
# check1 = doNotFindIt not in myList
# print (check1) # returns True

# # search a list for some particular elements
# if ("B" in myList) :
#     print ("item was located")
# if ("1" in myList) :
#     print ("item was located")
# else :
#     print ("item was NOT located")

# # ---------------------Sequential Linear Search----------------------------------- #
# implementation of a Linear Search
# time complexity ( Order of Magnitude ) : O(n)

def LinearSearchWithPrinting(sortedList, n):
    x = int(input("Enter the number to search: "))
    # Boolean Flag
    found = False
    for i in range(len(sortedList)) :
        if(sortedList[i] == x) :
            found = True
            print("%d found at %dth position" % (x, i))
            break
        if (found == False) :
            print("%d is not in %dth position" % (x, i))

# # -----------------------------------Binary Search-------------------------------- #
# implementation of a Binary Search
# time complexity ( Order of Magnitude ) : O(1) (iterative method) O(log n) (recursive method)
def binarySearchWithPrinting(sortedList, n):
    def binarySearch(sortedList, n, x) :
        start = 0
        end = n - 1
        while(start <= end) :
            mid = int((start + end) / 2)
            if (x == sortedList[mid]) :
                return mid
            elif(x < sortedList[mid]) :
                end = mid - 1
            else :
                start = mid + 1
        return -1

    x = int(input("Enter the number to search: "))
    position = binarySearch(sortedList, n, x)

    if (position != -1) :
        print("element number %d is present at position: %d" % (x, position))
    else :
        print("element number %d is not present in the list" % x)

# --------------------------------------Bubble Sort----------------------------------- #
# program for implementing a Bubble Sort

def bubbleSortWithPrinting(arr, n):
    def bubbleSort(arr, n) :
        # Traverse through all array elements
        for i in range(n - 1) :
        # range(n) also work but outer loop will repeat one time more than necessary
            # Last i elements are already in place
            for j in range(0, n - i - 1) :
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    bubbleSort(arr, n)
    print ("the sorted array is:")
    for i in range(len(arr)) :
        print ("%d" %arr[i])
    return arr

# # -----------------------------------Selection Sort----------------------------------- #
# # Routine for a Selection Sort

# A = ['t','e','s','t','d','a','t','a']

# for i in range(len(A)) :
#     min_= i
#     for j in range(i + 1, len(A)) :
#         if (A[min_] > A[j]) :
#             min_ = j
#     # swap performed
#     A[i], A[min_] = A[min_], A[i]

# # main
# for i in range(len(A)) :
#    print (A[i])

# -----------------------------------Insertion Sort----------------------------------- #


# -------------------------------------Menu------------------------------------------- #
# menu variables
select = 0
userList = []
isSorted = 0
n = 0

# -----------------------------Menu Helper------------------------------ #
def DisplayMenu() :
    print ("enter your choice")
    print ("1 for a Linear Search")
    print ("2 for a Binary Search")
    print ("3 for a Bubble Sort")
    print ("4 for a Selection Sort")
    print ("5 for a Insertion Sort")
    print ("6 to enter a new List")

# -----------------------------Select Helper---------------------------- #
def SelectRoutine() :
    global select, userList, isSorted, n

    DisplayMenu()
    select = int(input())
    if (select == 1) :
        print ("Call the Linear Search Routine")
        LinearSearchWithPrinting(userList, n)
        SelectRoutine()
    elif (select == 2 and isSorted == 1) :
        print ("Call the Binary Search Routine")
        binarySearchWithPrinting(userList, n)
        SelectRoutine()
    elif (select == 2 and isSorted == 0) :
        print ("Please select a sort routine before using Binary Search or use Lineat Search")
        SelectRoutine()
    elif (select == 3) :
        print ("Call the Bubble Sort Routine")
        userList = bubbleSortWithPrinting(userList, n)
        isSorted = 1
        SelectRoutine()
    elif (select == 4) :
        print ("Call the Selection Sort Routine")
        #selectionSortWithPrinting(userList, n)
    elif (select == 5) :
        print ("Call the Insertion Sort Routine")
        #insertionSortWithPrinting(userList, n)
    elif (select == 6) :
        print ("Input a new List!")
        listInput()
    else :
        print("invalid selection")

# -----------------------------Input List------------------------------- #
def listInput():
    global select, userList, isSorted, n

    isSorted = int(input("Enter 1 if your list is sorted and 0 if not: "))
    if (isSorted != 1 & isSorted != 0) :
        print("invalid selection")
        isSorted = int(input("Enter 1 if your list is sorted and 0 if not: "))

    n = int(input("Enter the size of your list: "))
    userList = []

    # populate the list in sort entry order
    for i in range(n) :
        userList.append(int(input("Enter %dth element: " % i)))
    SelectRoutine()

listInput()
