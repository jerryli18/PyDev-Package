'''
Created on Jan 20, 2015

@author: Jerry (jl585)

'''
def calculate(weight,height):
    """
    return float indicating BMI
    (body mass index)    
    given weight in pounds (float)
    given height in inches (float)
    """
      
    # you write code here
    BMI = 703.0695 * weight/(height**2)
    
    return BMI
  
