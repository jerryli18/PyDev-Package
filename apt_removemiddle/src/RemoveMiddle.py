'''
Created on Jan 28, 2015

@author: Jerry
'''
def shorten(name):
    """
    return the name with the middle name(s) removed. 
    name has at least one word. 
    """
      
    # you write code here
    
    a = name.split()
    if len(a) == 1:
        return a[0]
    else:
        return a[0]+" "+ a[len(a)-1]