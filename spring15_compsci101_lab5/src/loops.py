'''
Created on Feb 14, 2015

@author: Susan
'''
def digitsSmallerThanSum(number, sum):
    total = 0
    pos = 0
    while total <= sum and pos <= len(number):# USE WHILE LOOP
        total += number[pos]# TODO: return digits from right side that are less than sum     
        pos += 1
    return total

def findFirst(phrase, letter):
    if len(phrase)==0:
        return -1
    # TODO: return first position of letter in phrase, or return -1
    return -1
       

print "a", findFirst("The tragedy of Romeo and Juliet", "a")
print "m", findFirst("The tragedy of Romeo and Juliet", "m")
print "z", findFirst("The tragedy of Romeo and Juliet", "z")
print "t", findFirst("The tragedy of Romeo and Juliet", "t")

print "digitsSmallerThanSum(5372173, 11)", digitsSmallerThanSum(5372173, 11) 
print "digitsSmallerThanSum(5372173, 2)", digitsSmallerThanSum(5372173, 2)
print "digitsSmallerThanSum(5372173, 15)", digitsSmallerThanSum(5372173, 15)
print "digitsSmallerThanSum(55555555, 32)", digitsSmallerThanSum(55555555, 32)
