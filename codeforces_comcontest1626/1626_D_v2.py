# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:26:31 2022

@author: Valiakmetov-AA
"""
import math
def delta(n):
    if n == 0:
        cur = 0
        delta = 1
    else:
       f = math.log2(n)
       cf = f//1
       if f == cf:
           cur = cf
           delta = 0
       else:
           cur = cf+1
           delta = int(2**cur - n) 
    return (delta, cur)
def sum(a, begin, end)           
t = int(input())
dicts = []
for i in range(t):
    d ={'n': int(input())}
    a = [int (it) for it in input().split()]
    a.sort()
    d.update({'a': a}) 
    dicts.append(d)

for d in dicts:
    n = d['n']
    a = d['a']
    sv = []
    prev = None 
    s = 0
    for i in range(len(a)):
        if prev == None:
            prev = a[i]
        if prev == a[i]:
            s+=1
        else:
            sv.append(s)
            prev = a[i]
            s=1
    if s>0:
        sv.append(s)
      
    alls = len(a)
    cur = math.log2(alls)
    if cur!=cur//1:
        cur+=1
    delta = 2**cur-alls + 1 + 1
    n1 = 2**cur
    s1 = alls
    while n1>0:
        for i in range(min(n1, alls)-1, min(n1-delta, alls-1)-1, -1):
            if i > 0 and a[i] == a[i-1]:
                continue
            s1 = i + 1
            cur2 =  
            
            
            