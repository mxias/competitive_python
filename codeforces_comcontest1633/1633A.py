# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:14:28 2022

@author: Valiakmetov-AA
"""

t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
for k in range(t):
    i = n[k]
    if i%7 == 0:
        print(i)
    else:
        d = i%7
        stri = str(i)
        l = stri[len(stri)-1]
        if len(stri) == 1:
            print(7)
        elif d <= int(l):
            print(stri[:-1] + str(int(l)-d))
        else:
            for d in range(9, -1, -1):
                e = stri[:-2] + str(d) + l
                if int(e)%7 == 0:
                    print(e)
                    break