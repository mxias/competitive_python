# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:09:46 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    n = int(input())
    dicts.append(n)
for n in dicts:
    s = ''
    if n%3 == 2:
        cur = '2'
    else:
        cur = '1'
    s = cur + s
    n-=int(cur)
    
    while n>0:
        if cur == '1':
            cur = '2'
        else:
            cur = '1'
        s = cur+s
        n-=int(cur)
    print(s)