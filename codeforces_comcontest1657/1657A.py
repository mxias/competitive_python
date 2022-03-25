# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:20:45 2022

@author: Valiakmetov-AA
"""
import math
t = int(input())
data = []
for i in range(t):
    x,y = map(int, input().split())
    data.append((x,y))
for (x,y) in data:
    if (x,y) == (0,0):
        print(0)
    elif math.sqrt(x**2 + y**2) == int(math.sqrt(x**2 + y**2)):
        print(1)
    else:
        print(2)