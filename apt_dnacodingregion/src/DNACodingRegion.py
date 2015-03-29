'''
Created on Mar 24, 2015

@author: Grant
'''

        
def findRegion(dna):
    a = "atg"
    b = ["taa", "tag", "tga"]
    position = 0
    if dna.find(a) != -1:
        dna = dna[(dna.find(a) + 3): ]
    else:
        return ""
    for nucleobase in dna:
        CODONS_YO = ""
        if position % 3 == 0 and dna[position:position + 3] in b:
            CODONS_YO = dna[ :position]
        else:
            position += 1
    return CODONS_YO

        