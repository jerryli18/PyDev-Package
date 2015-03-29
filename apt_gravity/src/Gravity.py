'''
Created on Jan 22, 2015

@author: Jerry
'''
def falling(time,velo):
    """
    return float indicating 
    number of meters an object has 
    fallen after being dropped/thrown
    with initial velocity given by 
    float parameter velo
    (given in meters/second)
    and after falling for float parameter 
    time seconds
    """
      
    g = 9.8
    d = velo*time + 0.5*g*time**2
    return d