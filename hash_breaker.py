import argparse
import hashlib
import shelve

def main(source, bible, forward = False):

    if(forward):
        # Prepare forward search attack and save values into db
        dict = shelve.open("hashes.dict", writeback = True)
        legalWords = WordList()
        md5 = hashlib.md5()

        # Get the next possible password string.
        password = legalWords.next()

        # Find the Hash of that String
        md5.update(str.encode(password))
        hash = md5.hexdigest()

        # Store the string in a file/database
        dict[password] = hash;

        dict.close;

        # TODO: A lot more. What is here is just me tinkering around
        # so I have an idea of how I want to implement this section.
        # Most of this code will be moved into its own function.
    else:
        # Do brute force attack, and do forward search attack if db file is present and no salt
        pass # TODO: Implement this section in brute_force()
    # end if

    print('Success')

# end main

def brute_force():
    pass
# end brute_force

class WordList():
    """ Finds all the possible strings that could have been used 
        as passwords and hands them out when they are needed.
        
        JACOB, you can implement this however you want, but for              
        now, I'm planning on using the next method to check the             <---------------- JACOB, READ THIS
        next password until you have given me all strings of length          
        5 or less and all strings in the Bible.
    """

    @classmethod
    def next(self):
        return "string"
    # end next

    @classmethod
    def has_next(self):
        return True
    # end next

# end WordList


if __name__ == "__main__":
    # Set the command-line arguments for the program
    parser = argparse.ArgumentParser(
            description = "Mercury is the web-server application of the HEEV project."
        )
    parser.add_argument(
            "-s",
            "--source",
            help = "Filename of the source file containing the hashed passwords.",
            default = "pa3hashes.txt",
        )
    parser.add_argument(
            "-b",
            "--bible",
            help = "Filename of the source file containing the Bible text.",
            default = "Bible.txt",
        )
    parser.add_argument(
            "-f",
            "--forward",
            help = "Tells the program to perform a forward search attack",
            action = "store_true",
            default = False,
        )
    args = parser.parse_args()
    main(source = args.source, bible = args.bible, forward = args.forward)
# end if