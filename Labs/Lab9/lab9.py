import random
# randomly select an item within a list of elements
myList1 = ["me", "you", "him", "her", "it"]
print (random.choice(myList1))
print ("\n")
# convert a list into a set ( to remove any duplicates )
myList2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
mySet1 = set(myList2)
print (mySet1)
print ("\n")
print (sorted(mySet1))
print ("\n")
# randomly select a subset of elements
samples = random.sample(mySet1, 6)
print (samples)
# sort the subset
sortedList = sorted(samples)
print ("\n")
print (sortedList)
print ("\n\n")

