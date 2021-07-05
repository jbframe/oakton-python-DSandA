from os import system
system("clear")

print("""
--------------------------------Remarks------------------------------------
Name: John Frame, Student Number: B02291550, Date: 7/3/2021
Lab # & Name: 8 - Classes: Deep Learning (Text & Sequences) - The Movie Script
Course: CSC 242 Python Data Structures
---------------------------------------------------------------------------
""")
from MovieScript.MovieScript import MovieScript


# the movie text and sequences
seq = []
seq.append("opening teaser sequence")
seq.append("main titles with theme song")
seq.append("the plot unfolds")
seq.append("meeting with the superiors")
seq.append("the gadgets are issued")
seq.append("the mission begins")
seq.append("a romance ensues")
seq.append("thwarted but persistent")
seq.append("physical confrontation with the enemy")
seq.append("the enemy is defeated")
seq.append("the loose ends unfold")
seq.append("on to the next mission")

# convert the sequence list to a dictionary

# create a new movie script object
ms = MovieScript()
ms.script = seq
theScript = ms.getScript()
for x in range(len(theScript)) :
    print (u"\u2022", theScript[x], end = "\n")
print ("\n")

ms.search(seq)
