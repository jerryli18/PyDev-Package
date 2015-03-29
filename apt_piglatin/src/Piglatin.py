'''
Created on Feb 5, 2015

@author: Jerry
'''
def convert(s):
    """
    return piglatin-ized string version
    of string parameter s
    """
    def vowel(s):
        if "a" in s:
            return True
        if "e" in s:
            return True
        if "i" in s:
            return True
        if "o" in s:
            return True
        if "u" in s:
            return True
    if vowel(s[0]):
        return s + "-way" 
    elif s[0] == 'q':
        return s[2:] + "-quay"
    else:
        for i in range(len(s)):
            if vowel(s[i]):
                return s[i:] + "-" + s[:i] + "ay"