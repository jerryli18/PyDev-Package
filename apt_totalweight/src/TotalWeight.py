'''
Created on Jan 22, 2015

@author: Jerry
'''
def weight3(ab,ac,bc):
    """
    return float indicating 
    the total amount of weight for objects a, b and c.
    You are given the combined weight of a and b 
    together as parameter ab, the combined weight of 
    a and c together as parameter ac,
    and the weight of b and c together with parameter bc.
    """
      
    total = (ab + bc + ac)/2
    return total