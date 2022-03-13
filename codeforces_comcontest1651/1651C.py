# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:21:39 2022

@author: Valiakmetov-AA
"""
t = int(input())
data = []
for i in range(t):
    n = int(input())
    a = [int(it) for it in input().split()]
    b = [int(it) for it in input().split()]
    data.append({'n':n, 'a':a, 'b':b})
for tup in data:
    n = tup['n']
    a = tup['a']
    b = tup['b']
    
    val_b = abs(a[0] - b[0])
    ind_b = 0
    val_e = abs(a[-1] - b[-1])
    ind_e = len(b)-1
    
    val_b_2 = val_b
    ind_b_2 = 0
    val_e_2 = val_e
    ind_e_2 = len(a)-1
    for i in range(len(b)):
        if abs(a[0] - b[i]) < val_b:
            val_b = abs(a[0] - b[i]) 
            ind_b = i
        if abs(a[i] - b[0]) < val_b_2:
            val_b_2 = abs(a[i] - b[0]) 
            ind_b_2 = i    
        if abs(a[-1] - b[i]) < val_e:
            val_e = abs(a[-1] - b[i]) 
            ind_e = i
        if abs(a[i] - b[-1]) < val_e_2:
            val_e_2 = abs(a[i] - b[-1]) 
            ind_e_2 = i
    s = 0
    s+=val_b
    s+=val_b_2
    s+=val_e
    s+=val_e_2
    if ind_b ==0:
        s-=val_b
    if ind_e ==len(b)-1:
        s-=val_e
    print(s)
        
    