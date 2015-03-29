'''
Created on Mar 24, 2015

@author: Grant
'''
def reversecomp(dna):
    """
    return String that is the reverse
    complement of the String parameter dna 
    """
    
    list = []
    for codon in dna:
        if codon == 'a':
            list.append('t')
        if codon == 't':
            list.append('a')
        if codon == ('c'):
            list.append('g')
        if codon == ('g'):
            list.append('c')
    list.reverse()
    return ''.join(list)