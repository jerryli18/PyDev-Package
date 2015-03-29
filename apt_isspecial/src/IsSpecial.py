'''
Created on Feb 5, 2015

@author: Jerry
'''
def lovely(ingrediants,inedible):
    """
    return int, number of items in 
    ingrediants, a string that are edible 
    using informaion from  inedible, a string
    """
    a = ingrediants.split()
    b = inedible.split()
    edibles = len(a)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                edibles -= 1
    
    return edibles
