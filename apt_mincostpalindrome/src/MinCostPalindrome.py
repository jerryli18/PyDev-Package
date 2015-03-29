'''
Created on Feb 24, 2015

@author: Jerry
'''
def getMinimum(s, oCost, xCost):
    """
    return int based on String s and ints oCost, xCost
    """
    average = s
    price = 0
    for a in range(len(average)/2):
        if average[a] == "x":
            if average[-a-1] == "o":
                return -1
            if average[-a-1] == "x":
                price += 0
            if average[-a-1] == "?":
                price += xCost
        elif average[a] == "o":
            if average[-a-1] == "x":
                return -1
            if average [-a-1] == "o":
                price += 0
            if average[-a-1] == "?":
                price += oCost
        elif average[a] == "?":
            if average[-a-1] == "x":
                price += xCost
            if average[-a-1] == "o":
                price += oCost
            if average[-a-1] == "?":
                if oCost > xCost:
                    price += xCost * 2
                if xCost >= oCost:
                    price += oCost * 2
    return price
