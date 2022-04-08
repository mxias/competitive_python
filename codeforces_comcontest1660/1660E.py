# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:13:06 2022

@author: Valiakmetov-AA
"""
def main():            
    t = int(input())
    data = []
    for i in range(t):
        input()
        n = int(input())
        arr = []
        for i in range(n):
            arr.append([int(it) for it in input()])
        data.append((n,arr))
    for (n,arr) in data:
        m = 0
        s = 0
        for c in range(n):       
            cur_sum = 0
            for i in range(n):    
                j = (i + c)%n
                cur_sum+=arr[i][j]
            s+=cur_sum
            if m<cur_sum:
                m = cur_sum
        s = s-m+n-m
        print(s)                        
main()
                    