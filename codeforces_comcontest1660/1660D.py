# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:11:57 2022

@author: Valiakmetov-AA
"""

def max_multi(arr):
    count_neg = 0
    count2 = 0
    for i in arr:
        if i < 0:
            count_neg+=1
        if i == 2 or i ==-2:
            count2+=1
    if count_neg%2==0:
        return(count2,0,0)
    cl = count2
    l = 0
    for i in range(len(arr)):
        if arr[i]==2 or arr[i]==-2:
            cl-=1
        l+=1
        if arr[i] < 0:
            break
    cr = count2
    r = 0     
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==2 or arr[i]==-2:
            cr-=1
        r+=1
        if arr[i] < 0:
            break
    if cl > cr:
        return(cl,l,0)
    else:
        return(cr,0,r)        
def main():            
    t = int(input())
    data = []
    for i in range(t):
        n = int(input())
        a = [int(it) for it in input().split()]
        data.append((n,a))
    for (n,a) in data:
        m = []
        arr = []
        for i in range(len(a)):
            if a[i] == 0: 
            # and len(arr) > 0:
               m.append((i-len(arr),arr))
               arr = []
            elif a[i] != 0:
                arr.append(a[i])
                if i == len(a)-1:
                    m.append((i-len(arr)+1,arr))
        p = 0
        r_left = 0
        r_right = len(a)
        for (left, arr) in m:
            (p_arr,l,r) = max_multi(arr)
            if p_arr>p:
                p = p_arr
                r_left = left + l
                r_right = len(a) - left - len(arr) + r
        print (' '.join([str(r_left), str(r_right)]))
main()
                
        
        
            
    