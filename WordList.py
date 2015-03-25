import itertools
class WordList():
    """ Finds all the possible strings that could have been used 
        as passwords and hands them out when they are needed.
        
        JACOB, you can implement this however you want, but for              
        now, I'm planning on using the next method to check the             <---------------- JACOB, READ THIS
        next password until you have given me all strings of length          
        5 or less and all strings in the Bible.
    """
    
    
    def __init__(self, bible = "Bible.txt"):
        self.bible = open(bible)
        permutationsOf1 = []
        permutationsOf2 = []
        permutationsOf3 = []
        permutationsOf4 = []
        permutationsOf5 = []
        charactersToUse = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        permutations = itertools.product(charactersToUse, repeat = 1)
        for x in permutations:
            permutationsOf1 += [''.join(x)]
        permutations = itertools.product(charactersToUse, repeat = 2)
        for x in permutations:
            permutationsOf2 += [''.join(x)]
        permutations = itertools.product(charactersToUse, repeat = 3)
        for x in permutations:
            permutationsOf3 += [''.join(x)]
        permutations = itertools.product(charactersToUse, repeat = 4)
        for x in permutations:
            permutationsOf4 += [''.join(x)]
        permutations = itertools.product(charactersToUse, repeat = 5)
        for x in permutations:
            permutationsOf5 += [''.join(x)]
        bibleWords = []
        bibleWordstemp = self.bible.read().split(' ')
        for item in bibleWordstemp:
            bibleWords += item.split('\n')
        bibleWordsUsed = []
        """get words longer or equal to 6 in length"""
        for i in bibleWords:
            if len(i) <= 6:
                continue
            bibleWordsUsed.append(i)
        self.wordsToCheck = []
        for x in permutationsOf1:
            self.wordsToCheck.append(x)
        for x in permutationsOf2:
            self.wordsToCheck.append(x)
        for x in permutationsOf3:
            self.wordsToCheck.append(x)
        for x in permutationsOf4:
            self.wordsToCheck.append(x)
        for x in permutationsOf5:
            self.wordsToCheck.append(x)
        for x in bibleWordsUsed:
            self.wordsToCheck.append(x)
        self.count = len(self.wordsToCheck)
    # end constructor

    def next(self):
        toReturn = str(self.wordsToCheck[self.count])
        return toReturn
    # end next

    def has_next(self):
        if self.count > 0:
            self.count -= 1
            return True
        return False
    # end next
# end WordList