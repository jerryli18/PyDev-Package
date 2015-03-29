'''
Created on Feb 24, 2015

@author: Jerry
'''
def theMin(room):
    """
    return integer minimal number of changes needed to
    make adjacent characters in String room different
    """
    i = 0
    count = 0
    while i < len(room)-1:
        if room[i] == room[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count 