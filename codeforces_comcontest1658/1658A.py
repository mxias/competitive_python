# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:40:43 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n = int(input())
    s = input()
    data.append((n,s))
for (n,s) in data:
    sum1 = 0
    lp = None
    for i in range(len(s)):
        ch = s[i]
        if ch == '0': 
            if lp!=None and i - lp <3:
                sum1+=(3-(i-lp))
            lp = i
    print (sum1)
        
        