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

# the movie text, characters and sequences
characters = ["Nick the bitcoin hacker", "Johnny the full stack drone engineer", "Lisa the psychologist", "ASIC the enemy AI"]

seq = []
# the script is built using a sequence of segment stored in an array
# each segment is an array with the following element [description, [characters], segment length, firstUnitDirectorsT/F]
seq.append(["opening teaser sequence", [characters[0]], 3, True])
seq.append(["main titles with theme song", [characters[0]], 4, True])
seq.append(["the plot unfolds", [characters[0], characters[1], characters[3]], 6, True])
seq.append(["meeting with the superiors", [characters[0], characters[1], characters[2]], 5, False])
seq.append(["the gadgets are issued", [characters[0], characters[1], characters[2]], 5, False])
seq.append(["the mission begins", [characters[0], characters[1], characters[2]], 8, True])
seq.append(["a romance ensues", [characters[1], characters[2]], 6, True])
seq.append(["subplot: the lead character starts a CS degree", [characters[2]], 3, False])
seq.append(["thwarted but persistent", [characters[0], characters[1], characters[2], characters[3]], 7, True])
seq.append(["subplot: the lead charter develops a quantum computer", [characters[2]], 4, True])
seq.append(["physical confrontation with the enemy", [characters[0], characters[1], characters[2], characters[3]], 5, True])
seq.append(["subplot: The quantum computer hacks into the enemy defences", [characters[2], characters[3]], 3, True])
seq.append(["the enemy is defeated", [characters[0], characters[1], characters[2]], 5, True])
seq.append(["the loose ends unfold", [characters[1], characters[2]], 4, False])
seq.append(["on to the next mission", [characters[0], characters[1], characters[2]], 2, False])


# create a new movie script object
ms = MovieScript()

# the the object's methods!
ms.setScript(seq)
ms.getScript()
ms.search(seq)
