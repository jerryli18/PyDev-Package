'''
Created on Mar 3, 2015

@author: Jerry
'''
def howMany(meals, restaurant):
    """
    This function has two parameters. The first, meals,
    is a list of strings with each in the format
    "name:restaurant" where name is the name of a 
    person, and restaurant the name of a restaurant the
    person has eaten a meal at. The second parameter is 
    restaurant, a string that is the name of a 
    restaurant. This function returns the number of 
    unique people who have eaten at the restaurant.
    """
    i = set([a for a in meals if restaurant in a])
    return len(i)
