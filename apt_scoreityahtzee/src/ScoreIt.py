'''
Created on Feb 5, 2015

@author: Jerry
'''
def maxPoints(toss) :
    """
    return int representing the maximal Yahtzee
    score based on rolls in integer list toss
    """
    score = 0
    for roll in toss:
            if roll*toss.count(roll) > score:
                score = roll*toss.count(roll)
    return score

print maxPoints([2,2,5,5,4])
                