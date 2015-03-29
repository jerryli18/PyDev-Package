'''
Created on Mar 4, 2015

@author: Jerry
'''
import random

def load_lines(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines
    
    
def get_words(filename, wordlength = 5):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist


    
#     if len(words) < 30:
#         for i,w in enumerate(words):
#             print i,"\t",w
            
# def wordlength():
#     length = (raw_input("How long should the word be?"))
#     length = length.strip()
#     length = length.strip('.')
#     length = length.strip(',')
#     length = int(length)
#     return length
    
def numberOfguesses():
    guess = (raw_input("How many guesses do you want?"))
    guess = guess.strip()
    guess = guess.strip('.')
    guess = guess.strip(',')
    guess = int(guess)
    return guess
    

def misses():
    miss = numberOfguesses()
    if letter not in word:
        miss -= 1
    print "misses left: " + miss
  
def category():
    print r"What category?"
    print r"Traditionally: press A"
    print r"The states: press B"
    print r"The countries: press C"
    category = raw_input("Common Web sites: press D")
    category.strip()
    category.strip(",")
    category.upper()
    if len(category) == 1:
        return category
    else:
        return category[0]
      


def user():
    playing = category()
    length = int(raw_input("How long should the word be?"))
    guess = (raw_input("How many guesses do you want?"))
    guess = guess.strip()
    guess = guess.strip('.')
    guess = guess.strip(',')
    guess = int(guess)
    guesses = []
    if playing == "A" or playing == "a":
        words = get_words("lowerwords.txt",length)
        word = random.choice(words)
    elif playing == "B" or playing == "b":
        words = get_words("states.txt",length)
        word = random.choice(words)
    elif playing == "C" or playing == "c":
        words = get_words("countries.txt",length)
        word = random.choice(words)
    elif playing == "D" or "d":
        words = get_words("websites.txt",length)
        word = random.choice(words)
    else:
        words = get_words("lowerwords.txt",length)
        word = random.choice(words)
    for i in range(0,len(word)):
        guesses += "_"
    blankspace = "".join(guesses)
    miss = guess
    print word
    a = []
    b = ["".join(a)]
    count1 = 0
    count2 = 0
    while "_" in blankspace:
        if count1 < count2 + 1:
            count1 += 1
        fork = int(raw_input("Press 1 to guess a letter or 2 to guess a word"))
        print blankspace
        if fork == 2:
            secret = raw_input("What word would you like to guess?")
            if  secret == word.lower() or secret == word.upper():
                blankspace = blankspace.replace("_","")
                print word
                print "You got it! Secret word is " + word
            else:
                miss -= 1       
                print "misses left: " 
                print miss
                print "no" +" "+ secret
                secret = "".join(secret)
                a += ["".join(secret)]
                a.sort
                a.sort(key = len, reverse = True)
                #b = ["".join(a)]
                print "guesses so far:"
                print a
        if fork == 1:
            for letter in word:
                while int(count1) != int(count2):
                    count2 += 1
                    letter = str(raw_input("What letter would you like to guess?"))
                    #b = ["".join(a)]
                    if len(letter) == 1:
                        a += letter
                        a.sort()
                        a.sort(key = len, reverse = True)
                        b += letter
                        print "guesses so far: "
                        print a
                        item = letter
                        if item.upper() not in word and item.lower() not in word:
                            miss -= 1       
                            print "misses left: " 
                            print miss
                            print "no" +" "+ item
                        for element in word:
                            if element == item.upper() or element == item.lower():
                                guesses[word.find(element)] = item
                                print "misses left: " 
                                print miss
                            index = 0
                            while word[index:].find(item) != -1:
                                index = index + 1 + word[index:].find(item)
                                guesses[index-1] = item 
                    else:
                        print "please enter only one letter at a time"      
                    blankspace = "".join(guesses)
                    print blankspace
            if "_" not in blankspace:
                print "You got it! Secret word is " + word
            if letter == word.lower() or letter == word.upper():
                print word
                print "You got it! Secret word is " + word
        if miss == 0:
            print "No misses left. Game over."
            return ''
           
            
                



# def user():
#     print "what's the word length?>",
#     n = int(raw_input())
#     words = get_words("lowerwords.txt",n)
#     print "read %d words whose length is %d" % (len(words),n)
#     one = random.choice(words)
#     print "choosing at random>",one
#     wordlength()
#     blankspace = wordlength() * "_"
#     print blankspace
#     numberOfguesses()
#     misses(guess)
# 
if __name__ == "__main__":
    user()