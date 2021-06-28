a = [12 , 18 , 23 , 25 , 29 , 32 , 35 , 40 , 58 , 66 ]

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

print("index of target", binarySearch(a, len(a), 18))