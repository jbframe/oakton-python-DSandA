class MovieScript(object) :
    # begin the class definition

    # declare a data element as a list
    script = []
    spyMovieKeyWords = ["enemy", "gadgets", "mission", "drone", "start", "space", "undercover", "disguise"]
    segmentCharacters = []
    isFirstUnitDirectors = []
    segmentLength = []

    # the class constructor
    # def __init__(self) :
    #     # pass
    #     print ("a class object has been constructed\n")

    # a class member function
    def getScript(self) :
        for x in range(len(self.script)) :
            print (u"\u2022", self.script[x], end = "\n")
            characters = ""
            for y in range(len(self.segmentCharacters[x])) :
                characters += self.segmentCharacters[x][y]
                characters += ", "
            characters = characters[:len(characters)-2]
            print("\t featuring: " + characters)
            length = str(self.segmentLength[x])
            print("\t segment length: " + length + " minutes")
            if self.isFirstUnitDirectors[x] == True :
                print("\t First Unit Directors")
            else :
                print("\t Second Unit Directors")
        print ("\n")

    # a class member function
    def setScript(self, script) :
        for i in script :
            self.script.append(i[0])
            self.segmentCharacters.append(i[1])
            self.segmentLength.append(i[2])
            self.isFirstUnitDirectors.append(i[3])

    # a class member search function
    def search(self, seq) :
        print ("please enter a keyword to search the movie sequences")
        print ("\n")
        keyword = input().strip()
        isFound = False
        for i in range(len(seq)) :
            if (keyword in seq[i][0]) :
                isFound = True
                print ("[keyword(s) found]")
                print ("in scene sequence number ", i + 1)
                print ("\"", seq[i][0], "\"")
        for i in range(len(self.spyMovieKeyWords)) :
            if (keyword in self.spyMovieKeyWords[i]) :
                isFound = True
                print ("[keyword(s) found]")
                print ("in Spy Movie Keyword list, index ", i)
        if isFound == False :
            print ("[keyword(s) NOT found]")
        print ("\n")

    # end the class definition