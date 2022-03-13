# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:24:20 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    s = input()
    c = input()
    data.append({'s':s, 'c':c})
for tup in data:
    s = tup['s']
    c = tup['c']
    i = None
    for j in range(len(s)):
        if s[j] == c and j%2 == 0:
            i = j
            break
    if i == None:
        print('NO')
    else:
        print('YES')