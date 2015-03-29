'''
Created on Mar 3, 2015

@author: Jerry
'''
def countall(words):
    count = 0
    count2 = 1
    newlist = []
    for string in words:
        newlist.append(string.lower())
    newlist += [" "]
    for string in range(len(newlist)-1):
        if newlist[string][0] == newlist[string+1][0]:
            count2 += 1
        elif count2 > 1:
            count2 = 1
            count += 1
    return count