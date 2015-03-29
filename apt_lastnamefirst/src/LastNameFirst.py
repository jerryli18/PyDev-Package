'''
Created on Jan 29, 2015

@author: Jerry
'''
def modify(name):
    """
    return the name with the last name first, followed by a comma,
    followed by the first name (if any), followed by the first letter of
    each remaining name with a period after each letter. 
    name has at least one word. 
    """
      
    a = name.split()
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[1] + ", " + a[0]
    else:
        name = " "
        for i in range(1,len(a)-1):
            if len(a[i]) != 1:
                name += a[i][0] + ". "
            else:
                name += a[i][0] + " "
        name = name.strip()
    return a[len(a)-1]+ ", " + a[0] + " " + name
 
