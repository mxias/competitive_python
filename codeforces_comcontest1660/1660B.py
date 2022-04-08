# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:06:26 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n = int(input())
    a = [int(it) for it in input().split()]
    data.append((n,a))
for (n,a) in data:
    max1 = 0
    max2 = 0
    for el in a:
        if el>max1:
            max2 = max1
            max1 = el
        elif el>max2:
            max2 = el
    if max1-max2 > 1:
        print('NO')
    else:
        print('YES')
            