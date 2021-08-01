from os import system
system("clear")

print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/10/2021
Lab # & Name: 10 - Simulating a Customer Queue at the Local Drive - Through
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")
from Queue.Queue import Queue
from PQ.PQ import PQ
# instantiate a class object
q = Queue()
pq = PQ()
# object uses methods of the class
q.enqueue("Customer 1")
q.enqueue("Doordash Customer 2")
q.enqueue("GrubHub Customer 3")
q.enqueue("Customer 4")
q.dequeue()
q.dequeue()
q.display()
