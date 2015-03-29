'''
Created on Feb 5, 2015

@author: Jerry
'''
def coins(pence):
    """
    return three-element integer list
    based on int parameter pence
    """
    pounds = pence/240
    pleftovers = pence%240
    shillings = pleftovers/12
    sleftovers = pleftovers%12
    pennies = sleftovers
    
    return [pounds, shillings, pennies]