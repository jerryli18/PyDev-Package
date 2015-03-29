'''
Created on Feb 5, 2015

@author: Jerry
'''
def numberTimesAppear(number,digit):
    """
    return number of occurrences of digit, an integer,
    in number, an integer
    """
    count = 0
    a = str(number)
    b = str(digit)
    for i in a:
        if i == b:
            count += 1
    return count
        