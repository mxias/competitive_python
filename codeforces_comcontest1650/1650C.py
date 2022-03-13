# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:52:47 2022

@author: Valiakmetov-AA
"""

def f(x,a):
    return x//a + x%a
t = int(input())
data = []
for i in range(t):
    input()
    n,m = map(int, input().split())
    cw = []
    for i in range(m):
        x,w = map(int, input().split())
        cw.append((x, w, i+1))
    data.append({'n':n, 'm':m, 'cw':cw})
    
for tup in data:
    n = tup['n']
    m = tup['m']
    cw = tup['cw']
    cw.sort(key = lambda st: st[1])
    cw = cw[:2*n]
    cw.sort(key = lambda st: st[0])
    coord = []
    sum = 0
    for j in range(n):
        l = cw[n-1-j]
        r = cw[n+j]
        coord.append((str(l[2]), str(r[2])))
        sum+=l[1]
        sum+=r[1]
    print(sum)
    for j in range(len(coord)-1,-1,-1):
        it = coord[j]
        print(' '.join(it))
        