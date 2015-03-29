'''
Created on Mar 17, 2015

@author: Jerry
'''
def score(listA,listB,listC):
    """
    return String based on three string list parameters
    """
    

    setA = set()
    setB = set()
    setC = set()
    scoreA = 0
    scoreB = 0
    scoreC = 0
    [setA.add(item) for item in listA]
    [setB.add(item) for item in listB]
    [setC.add(item) for item in listC]
    for item in setA:
        if item not in setB.union(setC):
            scoreA += 3
        elif item in (setB.symmetric_difference(setC)):
            scoreA += 2
        elif item in (setB.intersection(setC)):
            scoreA += 1
    for item in setB:
        if item not in setA.union(setC):
            scoreB += 3
        elif item in (setA.symmetric_difference(setC)):
            scoreB += 2
        elif item in (setA.intersection(setC)):
            scoreB += 1
    for item in setC:
        if item not in setB.union(setA):
            scoreC += 3
        elif item in (setB.symmetric_difference(setA)):
            scoreC += 2
        elif item in (setB.intersection(setA)):
            scoreC += 1
    scoreA = str(scoreA)
    scoreB = str(scoreB)
    scoreC = str(scoreC)
    return scoreA + "/" + scoreB + "/" + scoreC
    