'''
All possible transform functions.

You need to complete this file.

Those whose name starts with transform_ will appear in the menu option.
You can write as many helper functions as you want to support these primary functions.

Created on Jan 30, 2015



@author: Jerry Li
'''



def transform_identity (word):
    '''Identity transform (no change).
       Note, this simply serves as an example transform.
    '''
    return word


def transform_uppercase (word):
    '''Transform to UPPERCASE (no decode).
       Note, this simply serves as an example transform.
    '''
    return word.upper()


def transform_pigify (word):
    '''Encode into Pig-latin from English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, this transformation is not unique, 
             some different words may be transformed into the same pig-latin word.
            
    '''
   #translates into Pig-Latin by searching for a vowel at the beginning of the word, "qu" at the beginning of the word
   #or assumes the word starts with a non-q consonant; in each case the function uses conditionals and then splices the word
     #and adds strings appropriately
    def vowel(word):
        if "a" in word:
            return True
        if "e" in word:
            return True
        if "i" in word:
            return True
        if "o" in word:
            return True
        if "u" in word:
            return True
    if vowel(word[0]):
        return word + "-way"
    elif word[0:2] == 'qu':
        return word[2:]+"-quay"
    else:
        for i in range(len(word)):
            if vowel(word[i]):
                return word[i:] + "-" + word[:i] + "ay"


def transform_unpigify (word):                  #searches for the endings of Pig-Latin and splices appropriately to convert into ENglish
    '''Decode from Pig-latin into English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, since some words may represent multiple different English words, 
             choose the final English word you think is more common.
    '''
    # TODO: complete this function so that it returns a new version of the string word,
    #       assuming word is in pig-latin, undo the pig-latin rules to decode the word to English
    def vowel(word):
        if "a" in word:
            return True
        if "e" in word:
            return True
        if "i" in word:
            return True
        if "o" in word:
            return True
        if "u" in word:
            return True
    if "way" in (word):
        return word[0:-4]
    elif word[-4] == "q":
        return "qu"+ word[0:-5]
    else:
        a = word.find("-")
        b = a+1
        return word[b:-2]+ word[0:a]


def transform_rot13 (word):                         #transforms into and from ROT13 by taking advantage of the fact that the lists are evenly split
    '''ROT-13 substitution cipher (both encodes and decodes).
       Note, since this transformation is symmetrical, 
       it can serve as encoder and decoder for the same message.
    '''
    # TODO: complete this function so that it returns a new version of the string word, 
    #       with each letter rotated by 13 places.
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    b = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    final = ""
    for s in word:
        i = a.find(s)
        final = final + b[i]
    return final
        
    



