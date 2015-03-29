'''
Created on Mar 3, 2015

@author: Jerry
'''
def getFortunate(a,b,c):
    """
    return int for parameters a,b,c,
    each parameter is a list of int values
    """
    
    match = []
    for i in a:
        for j in b:
            for k in c:
                sum = i+j+k
                if fortunate(sum) == True:
                    match.append(sum)
    return len(set(match))

def fortunate(sum):
    numbers = [0,1,2,3,4,6,7,9]
    for num in numbers:
        if str(num) in str(sum):
            return False
    return True