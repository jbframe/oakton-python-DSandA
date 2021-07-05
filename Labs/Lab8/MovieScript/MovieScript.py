class MovieScript(object) :
    # begin the class definition

    # declare a data element as a list
    script = []

    # the class constructor
    def __init__(self) :
        # pass
        print ("a class object has been constructed\n")

    # a class member function
    def getScript(self) :
        return self.script

    # a class member function
    def setScript(self, s) :
        script = s

    # a class member search function
    def search(self, seq) :
        print ("please enter a keyword to search the movie sequences")
        print ("\n")
        keyword = input().strip()
        isFound = False
        for i in range(len(seq)) :
            if (keyword in seq[i]) :
                isFound = True
                print ("[keyword(s) found]")
                print ("in scene sequence number ", i + 1)
                print ("\"", seq[i], "\"")
        if isFound == False :
            print ("[keyword(s) NOT found]")
        print ("\n")

    # end the class definition