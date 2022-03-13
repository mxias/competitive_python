# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:34:43 2022

@author: Valiakmetov-AA
"""
def f(x,a):
    return x//a + x%a
t = int(input())
data = []
for i in range(t):
    l,r,a = map(int, input().split())
    data.append((l,r,a))
for (l,r,a) in data:
    p = a*(r//a - 1) + a - 1
    if p>=l:
        print(max(f(p,a), f(r,a)))
    else: 
        print(f(r,a))
    