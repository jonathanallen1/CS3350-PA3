class WordList():
    """ Finds all the possible strings that could have been used 
        as passwords and hands them out when they are needed.
        
        JACOB, you can implement this however you want, but for              
        now, I'm planning on using the next method to check the             <---------------- JACOB, READ THIS
        next password until you have given me all strings of length          
        5 or less and all strings in the Bible.
    """

    def __init__(self, bible = "Bible.txt"):
        self.count = 1
        self.bible = bible
    # end constructor

    def next(self):
        return "string"
    # end next

    def has_next(self):
        if self.count > 0:
            self.count -= 1
            return True

        return False
    # end next
# end WordList