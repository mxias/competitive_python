# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:14:10 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    n = int(input())
    a = [int (it) for it in input().split()]
    d = {'n':n, 'a':a}
    dicts.append(d)
for d in dicts:
    n = d['n']
    a = d['a']
    a.sort()
    sumb = a[0]
    sumr = 0
    index_l = 1
    index_r = len(a)-1
    was_breaked = False
    while index_l < index_r:
        sumb+=a[index_l]
        sumr+=a[index_r]
        if sumb < sumr or sumr - sumb > a[index_r] - a[index_l]:
            print('YES')
            was_breaked = True
            break
        index_l+=1
        index_r-=1
    if not was_breaked:
        print('NO')
    # index = int(n/2) + 1
    # b = a[:index]
    # r = a[index:]
    # sumb = sum(b)
    # sumr = sum(r)
    # for i in range(0, min(len(r), len(b))):
    #     sumb-=b[len(b)-1-i]
    #     sumr-=r[i]