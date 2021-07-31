class Queue() :

    # construct the list to implement the queue
    def __init__(self) :
        self.queue = []

    # enqueue an element
    def enqueue(self, item) :
        self.queue.append(item)

    # remove an element from the queue
    def dequeue(self) :
        if (len(self.queue) < 1) :
            return None
        customer = self.queue.pop(0)
        print(customer + " is now being served.")
        return customer

    # display the current queue
    def display(self) :
        print(self.queue)

    # return the size of the queue
    def size(self) :
        return len(self.queue)
