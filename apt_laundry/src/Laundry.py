'''
Created on Jan 28, 2015

@author: Jerry
'''
def minutesNeeded(m): 
    """
    Return integer number of minutes to launder m (integer) loads
    """

    # with each load, time increases by 25 min
    
    if m == 0:
        return 0
    else:
        return 25+25+10+25*(m-1)
    