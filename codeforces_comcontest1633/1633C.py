# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 02:18:33 2022

@author: Valiakmetov-AA
"""
def LeftRight(Hc, Dc, Hm, Dm, k, w, a, kw):
    left = Hm/(Dc + w*kw)
    right = 1 + (Hc + a*(k-kw))/Dm
    return (left, right)
def IsGood(left, right):
    Zleft = int(left)
    if (Zleft != left):
        Zleft+=1
    if right > Zleft:
        return True
    return False             
t = int(input())
dicts = []
for i in range(t):
    (Hc, Dc) = [int (it) for it in input().split()]
    (Hm, Dm) = [int (it) for it in input().split()]
    (k, w, a) = [int (it) for it in input().split()]
    d = {'Hc':Hc, 'Dc':Dc, 'Hm':Hm, 'Dm':Dm, 'k':k, 'w':w, 'a':a}
    dicts.append(d)
for d in dicts:
    (Hc, Dc, Hm, Dm, k, w, a) = (d['Hc'], d['Dc'], d['Hm'], d['Dm'], d['k'], d['w'], d['a'])
    
    kw = k
    (left1, right1) = LeftRight(Hc, Dc, Hm, Dm, k, w, a, kw)
    if IsGood(left1, right1):
        print('YES')
        continue
    kw = 0
    (left2, right2) = LeftRight(Hc, Dc, Hm, Dm, k, w, a, kw)
    if IsGood(left2, right2):
        print('YES')
        continue
    i = int(left1) + 1
    yes = False
    while i < left2:
        temp = (Hm/i - Dc)/w
        if int(temp) != temp:
            kw = int(temp)+1
        else:
            kw = int(temp)
        (left, right) = LeftRight(Hc, Dc, Hm, Dm, k, w, a, kw)
        if IsGood(left, right):
            print('YES')
            yes = True
            break
        i+=1
    if not yes:
        print('NO')   