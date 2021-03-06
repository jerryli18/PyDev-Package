'''
Created on Sep 18, 2012

@author: ola
'''
import random

def walk(n):
    '''
    Simulate a one-dimensional walk on a grid from -n to n (2n+1 locations)
    Returns the number of steps needed to reach all 2n+1 locations
    '''
    
    # store a 0 if location not visited, 1 if it is visited
    locs = [0]*(2*n+1)
    
    current = 0   # current location, start at origin
    steps = 0     # the number of steps taken
    
    while sum(locs) != 2*n+1:
        steps = steps + 1
        locs[current+n] = 1


        if random.randint(1,2) == 1:
            current = current + 1
        else:
            current = current - 1
        if current > n:
            current = -n
        if current < -n:
            current = n
    return steps

def trials():

    trials = 100
    steps = 5
    runs  = []

    for i in range(trials):
        runs.append(walk(steps))
    print 1+2*steps,1.0*sum(runs)/trials


if __name__ == '__main__':
    trials()
