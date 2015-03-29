'''
Created on Feb 5, 2015

@author: Jerry
'''
def replace(phrase, newword):
    """
    return a string in which the first half of 
    each word in the string parameter phrase is
    replaced by the string parameter newword
    """
    answer = ""
    list = phrase.split()
    for word in list:
        middle = len(word)/2
        answer += newword + word[middle:] + " "
    return answer.strip()