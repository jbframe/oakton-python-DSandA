class PQ() :

    # construct the list to implement the queue
    def __init__(self) :
        self.pq = []

    # enqueue an element
    def enqueue(self, priority, item) :
        self.pq.append([priority, item])

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

    # return the current queue
    def returnQueue(self) :
        return self.pq

    # return the size of the queue
    def size(self) :
        return len(self.queue)

    # sync with
    def syncAndPrioritize(self, queue) :
        indexToSync = 0
        while len(queue) > len(self.pq) :
            self.pq.append([0,''])
        for i in queue :
            # if customer is in both queues
            if i == self.pq[indexToSync][1] :
                if self.pq[indexToSync][0] :
                    indexToSync += 1
                    continue
                else :
                    #set priority
                    self.pq[indexToSync][0] = input("What is the priority of " + i + "? ")
                    indexToSync += 1
                    continue
            # if customer is in not in the priority queue
            else :
                self.pq[indexToSync] = []
                self.pq[indexToSync].append(input("What is the priority of " + i + "? "))
                self.pq[indexToSync].append(i)
                indexToSync += 1