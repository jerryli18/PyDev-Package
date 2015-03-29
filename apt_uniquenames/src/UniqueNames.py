'''
Created on Mar 17, 2015

@author: Jerry
'''
def namesForYear(courses, year):
    """
    courses is a list of strings, each string represents a 
    course in the format course name followed by pairs of 
    student names and the year of the student with ":" 
    the separator.  For example:
      "courseName:name1:year1:name2:year2:name3:year3"
    
    year is the year of the student such as firstyear, 
    sophomore, junior, senior.
    
    return a string of the unique names in sorted order that 
    match year, with the names separated by blanks.
    """
    students = set()
    for course in courses:
        count = 0
        for info in course.split(':'):
            if info == year:
                students.add(course.split(':')[count - 1])
            count += 1
    students = sorted(students)
    answer = ""
    for name in students:
        answer += name+ " "
    return answer.strip()