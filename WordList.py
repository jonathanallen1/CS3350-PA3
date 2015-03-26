from itertools import product
from enum import Enum
import string

class Mode(Enum):
    PERMUTATIONS = 1
    BIBLE = 2
    DONE = 3
# end class Mode

class WordList():
    """ Finds all the possible strings that could have been used 
        as passwords and hands them out when they are needed.
        
        JACOB, you can implement this however you want, but for              
        now, I'm planning on using the next method to check the
        next password until you have given me all strings of length          
        5 or less and all strings in the Bible.
    """
    MAX = 5
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                '0','1','2','3','4','5','6','7','8','9']
    
    def __init__(self, bible = "Bible.txt"):
        self.bible = bible
        self.mode = Mode.PERMUTATIONS
        
        self.length = 1
        self.wordsToCheck = product(WordList.alphabet, repeat = self.length)
        val = self.wordsToCheck.__next__()
        self.next = str(val).replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(" ", "")

    # end constructor

    def getNext(self):
        toReturn = self.next

        if self.mode is Mode.PERMUTATIONS:
            try:
                val = self.wordsToCheck.__next__()
                self.next = str(val).replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(" ", "")
            except StopIteration:
                self.length += 1
                if self.length > WordList.MAX:
                    self.mode = Mode.BIBLE
                    self.next = "string"

                    bibleFile = open(self.bible)
                    self.bibleWords = []
                    noPunctuation = {ord(c): None for c in string.punctuation}
                    for line in bibleFile:
                        for word in line.split():
                            if len(word) > 5:
                                self.bibleWords.append(str(word).translate(noPunctuation).lower())

                    bibleFile.close()
                    self.index = 0
                    self.next = self.bibleWords[self.index]
                else:
                    self.wordsToCheck = product(WordList.alphabet, repeat = self.length)
        elif self.mode is Mode.BIBLE:
            toReturn = self.next

            self.index += 1
            if self.index >= len(self.bibleWords):
                self.mode = Mode.DONE
            else:
                self.next = self.bibleWords[self.index]

        return toReturn
    # end next

    def has_next(self):
        if self.mode is Mode.DONE:
            return False
        return True
    # end next
# end WordList