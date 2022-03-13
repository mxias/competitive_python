# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:03:29 2022

@author: Valiakmetov-AA
"""

t = int(input())
data = []
for i in range(t):
    data.append(int(input()))
for n in data:
    print(2**n-1)    