# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:33:16 2022

@author: Valiakmetov-AA
"""
# 13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        n = 0
        cont = False
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if cont:
                cont = False
                continue
            ch = s[i]
            next_ch = None
            if i < len(s)-1:
                next_ch = s[i+1]
            r = d[ch]
            if ch == 'I' and next_ch in ['V', 'X'] or ch == 'X' and next_ch in ['L','C'] or ch == 'C' and next_ch in ['D','M']:
                r = d[next_ch]-r
                cont = True
            n+=r
        return n
s = Solution()
n = s.romanToInt('MDCCCLIII')
                
        