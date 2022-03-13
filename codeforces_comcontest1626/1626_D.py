# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:05:19 2022

@author: Valiakmetov-AA
"""
import math

# def delta(n, cur = None):
#    if n == 0:
#        cur = 0
#        return 1
#    f = math.log2(n)
#    cf = f//1
#    if f == cf:
#        cur = cf
#        delta = 0
#    else:
#        cur = cf+1
#        delta = int(2**cur - n)
#    return delta
def delta2(n, cur = None):
   if n == 0:
       cur = 0
       return 1
   if cur == None:
       f = math.log2(n)
       cf = f//1
       if f == cf:
           cur = cf
           delta = 0
       else:
           cur = cf+1
           delta = int(2**cur - n)
   else:
       up = 2**cur
       lo = 2**(cur-1)
       if up < n:
           while up < n:
               cur+=1
               up = 2**cur
               lo = 2**(cur-1)
           delta = up - n
       elif lo < n and up>=n:
          delta = up - n
       else:
           while lo>=n:
               cur-=1
               up = 2**cur
               lo = 2**(cur-1)
           delta = up - n
           
           
   return delta
t = int(input())
dicts = []
for i in range(t):
    d ={'n': int(input())}
    a = [int (it) for it in input().split()]
    a.sort()
    d.update({'a': a}) 
    dicts.append(d)

for d in dicts:
    n = d['n']
    a = d['a']
    alls = len(a)
    s1=0
    delt = None
    breaked = False
    cur1 = None
    for i in range(n+1):
        if breaked:
            break
        if i < n:
            x = a[i]
        if i>0:
            s1+=1
        if i < n and i-1>=0 and a[i-1] == a[i]:
            continue
        #if cur1 == None:
        deltas1 = delta2(s1, cur1)
        # else:
        #     ms1 = 2**cur1
        #     if ms1 >= s1:
        #         deltas1 = ms1 - s1
        #     else:
        #         deltas1 = delta(s1, cur1)    
        if  delt != None and delt <= deltas1:
            continue
        s2=0
        cur2 = None
        cur3 = None
        for j in range(i,n+1):
            if j < n and i==j: 
                if j>0 and a[j]-a[j-1]>1 or j==0 and a[0]>2:
                    s2=0
                else:
                    continue
            elif j==n:
                s2 = 0
            else:                
                s2+=1
            if j < n and j-1>=0 and a[j-1] == a[j]:
                continue 
            s3 = alls-s1-s2
            deltas2 = delta2(s2,cur2)  
            if delt != None and delt <= deltas2:
                continue
            newdelta = deltas1 + deltas2 + delta2(s3, cur3)
            if delt == None or delt > newdelta:
                delt = newdelta
            if delt == 0:
                breaked = True
                break
    print(delt)
            
                