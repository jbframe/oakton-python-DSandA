print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/3/2021
Lab # & Name: 7 - Classes and Interfaces: A Bag Data Structure
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")

class Bag(object) :
    def __init__(self, maxsize = 10) :
        self.maxsize = maxsize
        self._items = list()
    def add(self, item) :
        if (len(self) >= self.maxsize) :
            raise Exception('Full')
        self._items.append(item)
    def remove(self, item) :
        self._items.remove(item)
    def __len__(self) :
        return len(self._items)
    def __iter__(self) :
        for item in self._items:
            yield item

def testBag() :
    bag = Bag()
    bag.add(10)
    bag.add("item 2")
    bag.add(30)
    assert len(bag) == 3
    bag.remove(10)
    assert len(bag) == 2
    # for i in bag :
    #     print (i)

if __name__ == "__main__" :
    testBag()

# -------------------------------------Menu------------------------------------------- #
# menu variables
select = 0
userBag = None

# -----------------------------Menu Helper------------------------------ #
def displayMenu() :
    global select, userBag
    print ("Enter your choice")
    print ("1 to add items to your bag")
    print ("2 to remove an item from your bag")
    print ("3 to check if an item is in your bag")
    print ("4 to check your bag capacity")

# -----------------------------Select Helper---------------------------- #
def selectRoutine() :
    global select, userBag
    displayMenu()
    select = int(input())
    if (select == 1) :
        elementToAdd = input("What item would you like to add:")
        userBag.add(elementToAdd)
        print("\nItem added!\n")
        selectRoutine()
    elif (select == 2) :
        elementToRemove = input("What item would you like to remove:")
        userBag.remove(elementToRemove)
        print("\nItem removed!\n")
        selectRoutine()
    elif (select == 3) :
        elToCheck = input("What item would you like to check for:")
        foundEl = False
        bagEmpty = True
        for el in userBag :
            bagEmpty = False
            if el == elToCheck :
                foundEl = True
                print("\nItem in bag!\n")
        if foundEl == True :
            print("\nItem IS in your bag!\n")
        else :
            print("\nItem IS NOT in your bag!\n")
        if bagEmpty == True :
            print("\n No items in your bag!\n")
        selectRoutine()
    elif (select == 4) :
        if len(userBag) == 10 :
            print("\nYour bag is at capacity!\n")
        elif len(userBag) == 1 :
            print("\nYou have " + str(len(userBag)) + " item in your bag!\n")
            print("There is room for 9 more!\n")
        else :
            print("\nYou have " + str(len(userBag)) + " items in your bag!\n")
            print("There is room for " + str(10 - len(userBag)) + " more!\n")
        selectRoutine()
    else :
        print("invalid selection")

select = input("Would you like a free beg? (Y/N)\n")
if (select != "Y" and select != "y" ) :
    print("We're sorry we couldn't offer you a bag today, come back any time\n")
else :
    userBag = Bag()
    selectRoutine()