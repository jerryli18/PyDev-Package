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
        artist = row[2]
        song = row[1]
        if artist not in d:
            d[artist] = []
        d[artist].append(song)
        print row
    info = d.items()
    tosort = [(len(t[1]),t[0]) for t in info]
    info = sorted(tosort)
    print info[-30:]

if __name__ == '__main__':
    dump("top1000.csv")