'''
Created on Jan 29, 2015

@author: Jerry
'''
def ratio(dna):
    """
    return float that's the cg ratio of the 
    nucleotides in the string parameter dna
    """

    count = 0.0
    for a in range(len(dna)):
        if(dna[a] == 'g' or dna[a] == 'c'):
            count += 1.0
    return count / len(dna)
