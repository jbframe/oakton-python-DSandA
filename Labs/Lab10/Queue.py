#  filename: Queue.py
classQueue() :
    # construct the list to implement the queue
    def __init__(self) :
        self.queue = []

    # enqueue an element
    def enqueue(self, item) :
        self.queue.append(item)

    # remove an element from the queue
    def dequeue(self) :
        if (len(self.queue) < 1) :
          returnNonereturnself.queue.pop(0)

    # display the current queue
    def display(self) :
        print(self.queue)