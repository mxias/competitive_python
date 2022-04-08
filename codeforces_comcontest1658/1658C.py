# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:18:19 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n = int(input())
    c = [int(it) for it in input().split()]
    data.append((n,c))
for (n,c) in data:
    count1 = 0
    isNo = False
    for i in range(len(c)):
        num = c[i]
        if num == 1:
            count1+=1
        if i == 0:
            prev = len(c)-1
        else:
            prev = i-1
        if count1 > 1 or num > c[prev]+1:
            isNo = True
            break
    if count1 == 0:
        isNo = True
    if isNo:
        print('NO')
    else: 
        print('YES')
        