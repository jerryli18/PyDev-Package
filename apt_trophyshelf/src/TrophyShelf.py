'''
Created on Mar 3, 2015

@author: Jerry
'''
def countVisible(trophies):
    rightLeft = 0
    maxvalue = 0
    
    rightCount = 0
    reversetrophies = trophies[::-1]
    maxright = 0
    
    for a in range(len(trophies)):
        if trophies[a] > maxvalue:
            rightLeft += 1
            maxvalue = trophies[a]
        if trophies[a] <= maxvalue:
            rightLeft += 0
            
    for b in range(len(reversetrophies)):
        if reversetrophies[b] > maxright:
            rightCount += 1
            maxright = reversetrophies[b]
        if reversetrophies[b] <= maxright:
            rightCount += 0
    return [rightLeft, rightCount]