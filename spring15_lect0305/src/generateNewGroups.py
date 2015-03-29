'''
Created on Oct 5, 2011, Modified Oct 20, 2014

@author: rodger
'''
import os
import tkFileDialog
import random

    
def choose_file_to_open():
    """
    prompt for existing file, return the file (open for reading)
    """
    file = tkFileDialog.askopenfile(title="choose a file", initialdir=os.getcwd())
    return file

def processFile(file):
    '''
    process the lines in a file (which has one name per line),
    return a list of names
    '''
    students = []
    for line in file:
        students.append(line.strip())
    return students
    
    
    
    
def randomize(students):
    '''
    shuffle the students in the list and return this new list
    '''
    randomstudents = []
    for stud in students:
        ind = random.randint(0,len(students)-1)    
        randomstudents.append(students[ind])
        students.pop(ind)
    print randomstudents





    return students

def printGroups(students):
    ''' print the students 3 per group with Group number starting w/1 '''
    count = 1
    print "Group 1"
    for stud in students:
        print stud
        if count%3 == 0:
            print "Group" + str(count/3+1)+ ":"
        count += 1
        
        
 


        count += 1

    

students = processFile(choose_file_to_open()) 
print students
randomize(students)       
print students
print
printGroups(students)
