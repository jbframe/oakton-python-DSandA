a = [4 , 8 , 19 , 2 , 28 , 21 ]

def selectionSortWithPrinting(arr, n):
    for i in range(n) :
        print(arr)
        min_= i
        for j in range(i + 1, n) :
            if (arr[min_] > arr[j]) :
                min_ = j
        # swap performed
        arr[i], arr[min_] = arr[min_], arr[i]

selectionSortWithPrinting(a, 6)