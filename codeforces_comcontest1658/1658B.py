# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:53:56 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n = int(input())
    data.append(n)
for n in data:
    if n//2 != n/2:
        print(0)
    else:
        rest = 1
        for i in range(n//2):
            rest = (rest*(i+1))%998244353
        rest = (rest**2)%998244353
        print(rest)