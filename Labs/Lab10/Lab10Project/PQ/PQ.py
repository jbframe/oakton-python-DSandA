class PQ() :

    # construct the list to implement the queue
    def __init__(self) :
        self.pq = []

    # enqueue an element
    def enqueue(self, priority, item) :
        self.queue.append([priority, item])

    # remove an element from the queue
    def dequeue(self) :
        if (len(self.pq) < 1) :
            return None
        customer = self.pq.pop(0)[1]
        print(customer + " is now being served.")
        return customer

    # display the current queue
    def display(self) :
        print(self.pq)

    # return the size of the queue
    def size(self) :
        return len(self.queue)
