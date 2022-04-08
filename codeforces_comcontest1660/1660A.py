# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:03:25 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    a,b = map(int, input().split())
    data.append((a,b))
for (a,b) in data:
    if a == 0:
        print(1)
    else:
        print(2*b+a+1)