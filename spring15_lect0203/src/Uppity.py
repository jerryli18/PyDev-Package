'''
Created on Sep 12, 2010, modified on Sep 17, 2014

@author: ola, modified by rodger
'''

def uppify_list(words):
    """ 
    Return a new list, based on parameter list
    but in which each string of parameter list 
    is represented by an upper case equivalent
    """
    newList = []
    for w in words:
        #TODO: Add code
        pass  # replace 
    return newList
    

def print_list(words):
    """
    print each element of words, a list, on a single line
    """
    for w in words:
        print w,
    print

    
def uppify_file(filename):
    """
    filename is name of a file, its contents are printed by
    converting each word to an uppercase equivalent
    and respecting lines, i.e., one line of output
    for each line of input. Whitespace is NOT 
    respected, i.e., white space separates line entries
    but isn't preserved in the output
    """
    # TODO: open file
    
    for line in file:
        # TODO: convert each line to a list of words
        #  Then call uppify_list to convert to uppercase
        # Then print the result, line by line     
        pass  #replace 
        
        
        
        
    file.close()

def main():
    filename = "../romeo.txt"
    uppify_file(filename)

if __name__ == "__main__":
    main()
