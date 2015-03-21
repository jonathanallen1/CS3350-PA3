import argparse
import hashlib
import shelve
from WordList import WordList

def main(source, bible, forward = False):
    # Get a list of all possible passwords.
    legalWords = WordList(bible)

    if(forward):
        # Prepare forward search attack and save values into db
        forward_search(legalWords)
        print("Forward search values stored in file hashes.dict.")
    else:
        # Do brute force attack and forward search attack if 
        # db file is present and there is no salt.

        # open the file with the usernames and hashes and read data from it
        f = open(source, "r");

        pass # TODO: Implement this section in brute_force()
    # end if

    # Print the total computation time
    print('Success')

# end main

def forward_search(legalWords):
    """ Performs a forward search attack for passwords with
        no salt by predetermining every possible password/
        hash combination and storing them in a data file.
    """

    # Open the dictionary file for writing.
    dict = shelve.open("hashes.dict", writeback = True)
    # Use md5 encryption
    md5 = hashlib.md5()

    while(legalWords.has_next()):
        # Get the next possible password string.
        password = legalWords.next()

        # Find the Hash of that String
        md5.update(str.encode(password))
        hash = md5.hexdigest()

        # Store the string in a file/database
        dict[hash] = password;
    # end while
        
    dict.close;
# end forward_search

def brute_force():
    pass
# end brute_force

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