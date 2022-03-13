# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:50:27 2022

@author: Valiakmetov-AA
"""

t = int(input())
s = []
for i in range(t):
    s.append(input())
for x in s:
    was_printed = False
    for j in range(len(x)-1, 0, -1):
        if (int(x[j]) + int(x[j-1]) > 9):
            print(x[:j-1] + str(int(x[j]) + int(x[j-1])) + x[j+1:])          
            was_printed = True
            break
    if not was_printed:
        print(str(int(x[0]) + int(x[1])) + x[2:])            