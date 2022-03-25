# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:40:31 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    n = int(input())
    a = [int(it) for it in input().split()]
    data.append((n,a))
for (n,a) in data:
   i = 0
   j = 0
   for k in range(len(a)):
       if a[k]>a[i]:
           i = k
       if a[k]<a[j]:
           j = k
   out = []
   out.append(str(i+1))
   out.append(str(j+1))
   print(' '.join(out))