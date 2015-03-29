'''
Created on Feb 24, 2015

@author: Jerry
'''
def whichOrder(available, orders):
    """
    return zero-based index of first
    sandwich in order, list of strings
    that can be made from ingredients
    in available, list of strings
    """
    
    
      
    for item in orders:
        count = 0
        items = item.split()
        for ingredient in items:
            if ingredient in available:
                count += 1
        if count == len(items):
            return orders.index(item)
        
    return -1   
    
    