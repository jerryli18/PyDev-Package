'''
Created on Feb 5, 2015

@author: Jerry
'''
def bagelCount(orders) :
       
    """
    return number of bagels needed to fulfill
    the orders in integer list parameter orders
    """

    count = 0
    for order in orders:
        if order < 12:
            count += order
        if order >= 12:
            count += order + int(order/12)
    
    return count