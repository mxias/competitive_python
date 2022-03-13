# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:41:43 2022

@author: Valiakmetov-AA
"""

t = int(input())
n = []
for i in range(t):
    n.append(input())
for i in range(t):
    s0 = 0
    s1 = 0
    for k in n[i]:
        if k == '0':
            s0+=1
        else:
            s1+=1
    if s0 < s1:
        print(s0)
    elif s0==s1:
        print(s0-1)
    else:
        print(s1)