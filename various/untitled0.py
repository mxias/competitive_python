# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 01:10:20 2022

@author: Valiakmetov-AA
"""
def RD(d):
    R = []
    D = []
    prev = None
    col = 0
    i = 0
    for ch in s:
        i+=1
        if prev != ch or i == len(s):
            if col > 0:
                if prev == "R":
                    R.append(col)
                else:
                    D.append(col)
            col = 0
        col+=1
        prev = ch
    if ch == "R":
        R.append(col)
    else:
        D.append(col)
    return (R,D)
def addCell(coords, curY, stepR):
    for i in range(stepR, 2*stepR+1):
        
t = int(input())
dicts = []
for i in range(t):
    n = int(input())
    d ={'n': n}
    d.update({'s': input()})
    dicts.append(d)
for d in dicts:
    n = d['n']
    s = d['s']
    (R,D) = RD(d)
    coords = []
    curX = 1
    curY = 1
    if s.startswith("D"):
        R.insert(0, 0)
    for stepR in R:
        
        for stepD in D:
                