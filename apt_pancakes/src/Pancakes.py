'''
Created on Jan 22, 2015

@author: Jerry
'''
def minutesNeeded (numCakes, capacity):
    """
    return integer representing time to cook pancakes
    based on integer parameters as described below
    """
    if numCakes == 0:
        return 0
    if numCakes == capacity: 
        return 10 
    if numCakes % capacity == 0:
        return (numCakes/capacity)*10
    if numCakes % capacity <= capacity/2:
        return (numCakes/capacity) * 10+5  
    if numCakes % capacity > capacity/2:
        return (numCakes/capacity) * 10 +10
    


