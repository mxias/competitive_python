# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:11:54 2022

@author: Valiakmetov-AA
"""

t = int(input())
dicts = []
for i in range(t):
    table = []
    n, m =map(int, input().split())
    for j in range(n):
        row = [int (it) for it in input()]
        table.append(row)
    dicts.append(table)
for table in dicts:
    No = False;
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            s = table[i-1][j-1] + table[i-1][j] + table[i][j-1] + table[i][j]
            if s == 3:
                No = True
                break
        if No:
            break
    if No:
        print('NO')
    else:
        print('YES')