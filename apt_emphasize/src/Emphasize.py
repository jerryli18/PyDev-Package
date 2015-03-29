'''
Created on Jan 29, 2015

@author: Jerry
'''
def repeat(word, number):
    """
      return the word with the first part of it repeated 
      if it is a valid part to repeat. The part to be 
      repeated must be repeated "number" times.
      If the first letter is not a vowel, and the third 
      letter is a vowel, then the part to repeat is the 
      first three letters.
      If the first and third letters are not vowels, but 
      the second letter is, then the part to repeat is 
      the first two letters. 
      Otherwise there is nothing to repeat. 
      Only the first letter of the returned word may be 
      a capital letter, if the original word started with 
      a capital letter. 
    """ 
    if len(word)== 1:
        return word
    if isVowel(word[0]):
        return word
    if len(word)== 2:
        if isVowel (word[1]):
            return word +word.lower() * (number-1)
        else:
            return word
    if len(word)== 3:
        if isVowel(word[2]):
            return word +word.lower() * (number-1)
        if isVowel(word[3]):
            return word + word.lower() * (number - 1)
    if len(word) > 3:
        if isVowel(word[2]):
            return word[:3] + word[:3].lower() * (number - 1) + word[3:]
        if isVowel(word[1]):
            return word[:2] + word[:2].lower() * (number - 1) + word[2:]
        return word

def isVowel(ch):
    ch = ch.lower()
    if ch == "a":
        return True
    if ch == "e":
        return True
    if ch == "i":
        return True
    if ch == "o":
        return True
    if ch == "u":
        return True
    return False
   

