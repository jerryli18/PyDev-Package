'''
Created on Mar 3, 2015

@author: Jerry
'''
def howManyLetters(phrase):
    """
    phrase is a string of words separated by blanks 
    
    return the number of unique letters that 
    are the first letter of some word
    """
    
    a = phrase.lower()
    b = a.split()
    c = set([i[0] for i in b])
    return len(c)