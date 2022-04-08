# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:19:27 2022

@author: Valiakmetov-AA
"""

# 10. Regular Expression Matching
class Solution(object):
    def charMatchblock(self, ch, block):
        return  block[0] == ch or block[0] == '.'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        blocks = []
        for i in range(len(p)):
            ch = p[i]
            if ch == '*':
                continue
            next_ch = ''
            if i < len(p)-1:
                next_ch = p[i+1]
                if next_ch != '*':
                    next_ch = ''
            blocks.append(ch+next_ch)
        lastp = set()
        lastp.add(-1)
        for ch in s:
            n_lastp = set()
            for i in lastp:
                if i == -1 or not blocks[i].endswith('*') :
                    i+=1 
                while i < len(blocks) and blocks[i].endswith('*'):
                    if self.charMatchblock(ch, blocks[i]) :
                        n_lastp.add(i)
                    i+=1
                
                if i<len(blocks) and self.charMatchblock(ch, blocks[i]):
                    n_lastp.add(i)
            if len(n_lastp) == 0:
                return False
            lastp = set(n_lastp)

        for i in lastp:
            thisCorrect = True
            for j in range(i+1, len(blocks)):
                if not blocks[j].endswith('*'): 
                    thisCorrect = False
            if thisCorrect:
                return True
        return False
                
            
s = Solution()
b = s.isMatch("aaa", "a*c*b")
                    