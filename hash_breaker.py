import argparse
import hashlib
import shelve
import os
import time
import itertools
from WordList import WordList

def main(source, bible, forward = False):
    # Mark the starting time of the program
    start = time.time()

    if forward:
        # Get a list of all possible passwords.
        legalWords = WordList(bible)

        # Prepare forward search attack and save values into db
        forward_search(legalWords)
        print("Forward search values stored in file hashes.dict.")
    else:
        # Do brute force attack and forward search attack if 
        # db file is present and there is no salt.

        # open the file with the usernames and hashes and read data from it
        fileObject = open(source, "r");
        
        for line in fileObject:
            legalWords = WordList(bible)
            separate = line.split(':')
            user = separate[0]
            salt = separate[1]
            hash = separate[2].strip()

            pwrd = brute_force(salt, hash, legalWords)
            print(user + " " + pwrd)
        # end for
    # end if

    # Print the total computation time
    print('total runtime in hours, minutes and seconds: ' + \
        time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

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

    while legalWords.has_next():
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

def brute_force(salt, hash, legalWords):

    if salt is '' and os.path.isfile("hashes.dict.dat"):
        dict = shelve.open("hashes.dict")
        if hash in dict.values():
            return dict[hash]
        # end if
    # end if

    while legalWords.has_next():
        pwrd = legalWords.next()
        
        # Find the Hash of that String
        if hashlib.md5(str.encode(pwrd + salt)).hexdigest() == hash:
            return pwrd
        # end if
    # end while

    return "-- Unable to find password. --"
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