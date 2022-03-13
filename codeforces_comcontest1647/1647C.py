# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:13:09 2022

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
    if table[0][0] == 1:
        print(-1)
    else:
        num = 0
        zerotable = []
        scoord = []
        for i in range(len(table)):
           zerotable.append([0]*len(table[0]))    
        for i in range(len(table)-1, -1, -1):
            for j in range(len(table[0])-1, -1, -1):
                if table[i][j] != zerotable[i][j]:
                    num+=1
                    zerotable[i][j] = table[i][j] 
                    coord = []
                    if j == 0:
                        zerotable[i-1][j] = 1 - zerotable[i][j]
                        coord.append(str(i))
                        coord.append(str(j+1))
                        coord.append(str(i+1))
                        coord.append(str(j+1))
                    else:
                        zerotable[i][j-1] = 1 - zerotable[i][j]
                        coord.append(str(i+1))
                        coord.append(str(j))
                        coord.append(str(i+1))
                        coord.append(str(j+1))
                    scoord.append(coord)
        print(num)
        for coord in scoord:
            print(' '.join(coord))