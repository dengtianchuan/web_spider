#!/usr/bin/python3
"""
created on May 25 2018
"""

import random

class Selectball(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = input("The number of testing:")
            try:
                num = int(numStr)
            except ValueError:
                print("Please input a number")
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(num):
            n = random.randint(1,10)
            ball[n-1] += 1
        for i in range(1,11):
            print("The probability of getting %dth ball is %f" %(i, ball[i-1]*1.0/num))

if __name__ == '__main__':
    SB = Selectball()
