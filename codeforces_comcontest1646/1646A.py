# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:56:26 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    (n, s) = map(int, input().split())
    dicts.append((n,s))
for d in dicts:
    n = d[0]
    s = d[1]
    print(int(s/(n*n)))