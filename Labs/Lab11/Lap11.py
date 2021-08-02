from os import system
system("clear")

print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/17/2021
Lab # & Name: 11 - Linked Lists and their Applications
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")

print("""---------------------------------------------------------------------------
List implementation of a Stack
---------------------------------------------------------------------------
""")

class Node :

    # singly linked node
    def __init__(self, data = None) :
        self.data = data
        self.next = None
        # print(data)

class Singly_linked_list :

    def __init__(self) :
        # create an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self) :
        # iterate through the list
        current_item = self.head
        while current_item :
            val = current_item.data
            current_item = current_item.next
            yield val

    def addToTail(self, data) :
        # append items on the list
        node = Node(data)
        if self.tail :
            self.tail.next = node
            self.tail = node
        else :
            self.head = node
            self.tail = node
        self.count += 1
        return data

    def removeTail(self) :
        # remove the tail of the list
        if self.head.data == None :
            return "Empty"
        if self.head.next == None :
            lastItem = self.head.data
            self.head.data = None
            self.count -= 1
            return lastItem
        secondLastItem = self.head
        while(secondLastItem.next.next) :
            secondLastItem = secondLastItem.next
        lastItem = self.tail.data
        self.count -= 1
        self.tail = secondLastItem
        self.tail.next = None
        return lastItem

class Stack :
    def __init__(self) :
        # create an empty stack
        self.stack = Singly_linked_list()

    def push(self, data) :
        # push an item on the stack
        return print("Push: " + str(self.stack.addToTail(data)))

    def pop(self) :
        # pop an item from the stack
        return print("Pop: " + str(self.stack.removeTail()))

    def peek(self) :
        # peek at the top of the stack
        return print("Peek: " + str(self.stack.tail.data))

    def size(self) :
        return print("Stack size: " + str(self.stack.count))



stack = Stack()
stack.push("item 1")
stack.size()
stack.push("item 2")
stack.size()
stack.push("item 3")
stack.size()
stack.push("item 4")
stack.size()
stack.push("item 5")
stack.size()
stack.push("item 6")
stack.size()
stack.peek()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.size()
stack.pop()