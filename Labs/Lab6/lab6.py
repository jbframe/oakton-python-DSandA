print("""
Name: John Frame, Student Number: B02291550, Date: 6/26/2021
Lab # & Name: 6 - More on Collections: Multi - Dimensional Arrays
Course: CSC 242 Python Data Structures
""")
import random
import pickle as pk
# a dictionary of genres
genres = {1: "hobby", 2: "romance", 3: "cooking", 4: "science", 5: "adventure", 6: "puzzles"}

#  list for magazine genres
floor1Genres = [6, 2, 5]
floor2Genres = [1, 4, 3]
floor3Genres = [2, 6, 5]
floor4Genres = [3, 1, 1]
floor5Genres = [2, 4, 3]
magGenres = [floor1Genres, floor2Genres, floor3Genres, floor4Genres, floor5Genres]

# random number lists for magazine qty
floor1QTY = [random.randrange(1, 51, 1) for i in range(3)]
floor2QTY = [random.randrange(1, 51, 1) for i in range(3)]
floor3QTY = [random.randrange(1, 51, 1) for i in range(3)]
floor4QTY = [random.randrange(1, 51, 1) for i in range(3)]
floor5QTY = [random.randrange(1, 51, 1) for i in range(3)]
magQTYs = [floor1QTY, floor2QTY, floor3QTY, floor4QTY, floor5QTY]

# dump the data
file1 = open("magQTYs.p", "wb")
file2 = open("magGenres.p", "wb")
pk.dump(magQTYs, file1)
pk.dump(magGenres, file2)
file1.close()
file2.close()

# load the data
file1 = open("magQTYs.p", "rb")
file2 = open("magGenres.p", "rb")
magQTYs = pk.load(file1)
magGenres = pk.load(file2)
file1.close()
file2.close()

print("Print the picked data:")
print ("The matrix of magazine genres is: " +  str(magGenres))
print ("The matrix of magazine quantities is: " +  str(magQTYs))

floorToCheck = int(input("Enter the floor (1-5) where you want to check inventory on: ")) - 1
roomToCheck = int(input("Enter the room (1-3) where you want to check inventory in: ")) - 1

print("The quantity for this room is: " + str(magQTYs[floorToCheck][roomToCheck]))
print("The genre for this room is: " + genres[magGenres[floorToCheck][roomToCheck]])
password = input("To check total magazine count enter the administration password: ")

totalMagCount = "no admin access"
if password == "password":
  totalMagCount = 0
  for i in range(len(magQTYs)):
    for j in range(len(magQTYs[i])):
      totalMagCount += magQTYs[i][j]
  print("The total magazine count is: " + str(totalMagCount))
else:
  print(totalMagCount)