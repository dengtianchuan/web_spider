#!/usr/bin/python3.5
"""
created on May 24 2018
"""

class PrintTable(object):
    '''Printing Table9x9'''
    def __init__(self):
        print("Starting to print Table9x9")
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print("%dX%d=%2d  " %(j,i,i*j))
            print("\n")

if __name__=="__main__":
    pt = PrintTable()
