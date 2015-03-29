'''
Created on Jan 29, 2015

@author: Jerry
'''
def acronym(phrase):
    """
    return a string that is an acronym of the string 
    parameter phrase
    """

    # you write code here
    
    def acronym(phrase):
        list = phrase.split()
        word = "" 
        for item in list:
            word = word + item(0)  
        return word