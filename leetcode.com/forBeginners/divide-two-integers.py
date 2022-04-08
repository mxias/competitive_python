# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:26:19 2022

@author: Valiakmetov-AA
"""
# 29. Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = - dividend
        if divisor < 0:
            sign = - sign
            divisor = - divisor
        if dividend < divisor:
            return 0
        first = divisor
        second = divisor + divisor
        i = 1
        while not(dividend >= first and dividend < second):
            i+=i
            first+=first
            second+=second
        # if dividend - first < second - dividend:
        i = i + self.divide(dividend - first, divisor)
        # else:
        #     i = i + i - self.divide(second - dividend, divisor) -1

        if sign < 0:
            i= -i
        if i > 2**31 - 1:
            i = 2**31-1
        if i < -2**31:
            i = -2**31
        return i
s = Solution()
r = s.divide(2147483648, -1)
            
     