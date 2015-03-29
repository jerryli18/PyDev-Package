'''
Created on Mar 3, 2015

@author: Jerry
'''
def getMaximumSubset(words):
    """
    return int value that represents
    size of largest anagram-free subset
    of values in words, a list of strings
    """
    a = set([''.join(sorted(i)) for i in words])
    return len(a)
