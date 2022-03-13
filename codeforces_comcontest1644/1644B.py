# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:34:30 2022

@author: Valiakmetov-AA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:25:25 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    d ={'n': int(input())}
    dicts.append(d)
for d in dicts:
    n = d['n']
    if n < 3:
        continue
    if n==3:
        print("1 3 2")
        print("2 3 1")
        print("3 2 1")
        continue
    m = []
    for i in range(n):
        m.append(n-i)
    for i in range(n):
        print(' '.join([str(it) for it in m]))
        m.insert(len(m)-1, m.pop(0))