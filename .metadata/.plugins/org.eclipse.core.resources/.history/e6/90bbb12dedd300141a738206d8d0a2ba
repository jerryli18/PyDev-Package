'''
Created on Oct 24, 2012

@author: ola
'''

import csv

def dump(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    d = {}
    for row in freader:
       print row
    


if __name__ == '__main__':
    dump("top1000.csv")