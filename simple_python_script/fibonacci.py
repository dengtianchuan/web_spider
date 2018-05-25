#!/usr/bin/python3.5
"""
created on May 24 2018
"""

class Fibonacci(object):
    """Return a fibonacci list"""
    def __init__(self):
        self.fList = [0,1]
        self.main()

    def main(self):
        listLen = input("please input the length of fibonacii list(3-50): ")
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print("The fibonacci list is:\n %s" %self.fList)

    def checkLen(self,lenth):
        lenList = map(str,range(3,50))
        if lenth in lenList:
            print("The input lenth is up to standard, keeping on running")
        else:
            print("Please input a number between 3-50, and it is unnecessary to input a bigger number")
            exit()

if __name__ == "__main__":
    f = Fibonacci()
