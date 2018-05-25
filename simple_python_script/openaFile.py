#!/usr/bin/python3
"""
created on May 25 2018
"""

import os

def operaFile():
    print("Creating a File named test.txt, and writing 'Hello Python' in it")
    print("It should promise that text.txt didn't exit")
    os.system('rm test.txt')
    os.system('ls -l test.txt')
    print("Creating the File and write it")
    fp = open('test.txt', 'w')
    fp.write('Hello Python')
    fp.close
    print("Don't forget to close the File")
    print("To see that if test.txt is exit, and check the content\n")
    os.system("ls -l test.txt")
    os.system("cat test.txt")
    print("\n")
    print("How to avoid the failure of opening File?")
    print("Just using with as")
    with open('test.txt', 'r') as fp:
        st = fp.read()
    print("The content of test.txt is:%s" %st)

if __name__ == '__main__':
    operaFile()
