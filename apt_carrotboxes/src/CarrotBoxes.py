'''
Created on Feb 24, 2015

@author: Jerry
'''

def theIndex(carrots,amount):
    """
    carrots is list of integers representing
    boxes of carrots, amount is int value. 
    return int that is the index/box number
    of the box from which the last of
    amount carrots are eaten
    """
    for a in range(1, amount):
        mostcarrots = carrots.index(max(carrots))
        carrots[mostcarrots] = carrots[mostcarrots] - 1
    for a in range(amount, amount + 1):
        mostcarrots = carrots.index(max(carrots))
        carrots[mostcarrots] = carrots[mostcarrots] - 1
    return mostcarrots
