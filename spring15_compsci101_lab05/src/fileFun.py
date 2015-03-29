'''
Created on Sep 21, 2014 by Susan Rodger

@author: rodger
@author: YOUR NAME HERE
'''

def printLines(filename):
    infile = open(filename, 'r')
    for line in infile:
        print line,  
    print       
    infile.close()


def numberWords(filename):
    # TODO: open file, count number of words in file, 
    # TODO:    close file, return number
    return 0

def numberLines(filename):
    # TODO: open file, count number of lines in file, 
    # TODO:    close file, return number
    return 0    

def numberOfWord(filename, word):
    # TODO: open file, count number of times word appears, 
    # TODO:    close file, return number
    return 0

def listAthletes(filename, sport):
    # TODO: open file, print athletes in sport, close file
    print "Athletes in", sport


def main():
    filename = "../data/simple.txt"
#    filename = "../data/lorax.txt"
#    filename = "../data/athletes.txt"
 
    printLines(filename)   
    print "Number of words:", numberWords(filename)
    print "Number of lines:", numberLines(filename)
    print "Number of times 'is' occurs", numberOfWord(filename, "is")
    print 
    listAthletes(filename, "soccer")
    print
    listAthletes(filename, "golf")

if __name__ == "__main__":
    main()