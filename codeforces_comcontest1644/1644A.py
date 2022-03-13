# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:25:25 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    d ={'s': input()}
    dicts.append(d)
for d in dicts:
    keys = []
    no = False
    for ch in d['s']:
        if ch in ['r', 'g', 'b']:
            keys.append(ch)
        elif not ch.lower() in keys:
            print('NO')
            no = True
            break;
    if not no:
        print('YES')    