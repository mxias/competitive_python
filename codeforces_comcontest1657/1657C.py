# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:13:18 2022

@author: Valiakmetov-AA
"""

def is_palindrome(string):
    if len(string) <= 1:
        return False
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
def get_pref(s, index):
    pref = ''
    count_o = 0
    count_c = 0   
    correct = True
    for i in range(index+1, len(s)):
        ch = s[i]
        pref+=ch
        if ch == '(':
            count_o+=1
        else:
            count_c+=1
        if count_c > count_o:
            correct = False
        if count_c == count_o and correct:
            return (pref, i)
        elif is_palindrome(pref):
            return (pref, i)
    return ('', index)
            
t = int(input())
data = []
for i in range(t):
    n = int(input())
    s = input()
    data.append((n,s))
for (n,s) in data:
    c = 0
   
    index = -1
    (pref, index) = get_pref(s, index)
    while pref != '':
        c+=1
        # s = s[len(pref):]
        (pref, index) = get_pref(s, index)
    a = []
    a.append(str(c))
    a.append(str(len(s[index+1:])))         
    print(' '.join(a))