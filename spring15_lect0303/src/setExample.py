'''
Created on Oct 7, 2014

@author: Susan
'''
'''
Created on Oct 17, 2011

@author: rodger
'''


def processList(stringList):
    '''
    process the list of strings to 
    return a list of lists
    remove the course number since it is not needed
    '''
    allLists = []
    for line in stringList:
        # TODO - replace the next line with code
        "remove this line"
        a = line.split()
        del a[0]
        allLists.append(a)

    return allLists
        
        
def peopleTakingCourses(data):
    ''' data is a list of lists of names for each course,
    return list of all strings that appear at least once '''
    names = set([])
    for lista in data:
        seta = set(lista)
        names = names | seta
    return list(names)
        
        
    
    
def unionAllSetsButMe(allsets, me): 
    ''' allsets is a list of sets of names, me is the index number of
    one of the sets in allsets, returns the union of all the
    sets except the set in position me '''
    answer = set([])
    for index in range(len(allsets)):
        if index != me:
            answer = answer | allsets[index]
    
    return answer   
    
    
def peopleTakingOnlyOneCourse(data):
    ''' data is a list of lists of names for each course,
    returns list of people taking only one course '''
    names = set([])
    listOfSets = [set(w) for w in data]
    
    for index in range(len(listOfSets)):
        #TODO
        "replace me"
        unionOtherCourses = unionAllSetsButMe(listOfSets, index)
        for person in listOfSets[index]:
            if person not in unionOtherCourses:
                names.add(person)
    return list(names)
            

    
    
courseListsAll = ["compsci101 Smith Ye Li Lin Abroms Black", \
"math101 Green Wei Lin Yavatkar Delong Noell Ye Smith", \
"econ101 Abroms Curtson Williams Smith", \
"french1 Wills Wrigley Olson Lee", \
"history230 Black Wrigley Smith"]    

allcourses = processList(courseListsAll)
print allcourses

allpersons = peopleTakingCourses(allcourses)
allpersons.sort()
print str(len(allpersons)) + " people taking one or more courses"
print allpersons

example = [set(["a", "b", "c"]), set(["b", "c", "d", "g"]), set(["e", "d", "a"])]

print example
print unionAllSetsButMe(example,1)

allonecourse = peopleTakingOnlyOneCourse(allcourses)
allonecourse.sort()
print str(len(allonecourse)) + " people taking only one course"
print allonecourse

