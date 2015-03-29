'''
Created on Feb 5, 2015

@author: Jerry
'''
def getMessage(original):
    """
    return String that is 'textized' version
    of String parameter original
    """
    list = original.split()
    v = ["a", "e", "i", "o", "u"]
    ansr = ""
    for w in list:
        if w.count("a") + w.count("e") + w.count("i") +w.count("o") +w.count("u") == len(w):
            ansr += w + " "
        else:
            x = 0
            for l in w:
                if l in v:
                    pass
                elif x == 0:
                    ansr += l
                elif w[x - 1] in v:
                    ansr += l
                x += 1
            ansr += " "
    return ansr.strip()