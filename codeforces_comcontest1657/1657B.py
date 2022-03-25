# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:14:29 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n,B,x,y = map(int, input().split())
    data.append((n,B,x,y ))
for (n,B,x,y) in data:
    a = []
    last = 0
    suma = 0
    for i in range(1, n+1):
        if last + x <=B:
            last+=x
        else:
            last-=y
        suma+=last
    print(suma)        