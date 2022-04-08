# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:46:30 2022

@author: Valiakmetov-AA
"""
# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pr = ''
        for i in range(min([len(x) for x in strs])):
            s = {x[i] for x in strs}
            if len(s) == 1:
                pr += s.pop()
            else:
                break
        return pr
s = Solution()
pr = s.longestCommonPrefix(['asdasd', 'asffdk', 'asllflf'])