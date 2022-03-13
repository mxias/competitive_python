# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 00:38:02 2022

@author: Valiakmetov-AA
"""
def value(arr, n):
    val = 0
    for i in range(n):
        for j in range(i+1,n):
            val+= (arr[i] + arr[j])**2
    return val
t = int(input())
dicts = []
for i in range(t):
    d ={'n': int(input())}
    a = [int (it) for it in input().split()]
    b = [int (it) for it in input().split()]
    d.update({'a': a})
    d.update({'b': b})
    dicts.append(d)
for d in dicts:
    n = d['n']
    a = d['a']
    b = d['b']
    val = value(a,n) + value(b,n)
    Sa = sum(a)
    Sb = sum(b)
    for i in range(n):
        beforeA = (n-1)*a[i]*a[i] + 2*a[i]*(Sa - a[i])
        afterA = (n-1)*b[i]*b[i] + 2*b[i]*(Sa - a[i])
        beforeB = (n-1)*b[i]*b[i] + 2*b[i]*(Sb - b[i])
        afterB = (n-1)*a[i]*a[i] + 2*a[i]*(Sb - b[i])
        
        if afterA + afterB < beforeA + beforeB:
            (a[i], b[i]) = (b[i], a[i])
            Sa = Sa - b[i] + a[i]
            Sb = Sb - a[i] + b[i]
            val = val - (beforeA + beforeB) + (afterA + afterB)
    print(val)