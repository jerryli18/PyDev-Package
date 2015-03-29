'''
Created on Mar 17, 2015

@author: Jerry
'''
def maxLength(letters):
    count = 0
    for a in range(len(letters)):
        for b in range(a, len(letters) + 1):
            if len(set(letters[a:b]))==len(letters[a:b]) > count:
                count = len(letters[a:b])
    return count