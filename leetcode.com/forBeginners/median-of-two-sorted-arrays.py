# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:55:23 2022

@author: Valiakmetov-AA
"""

# 4. Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2))%2 == 0:
            k1 = (len(nums1) + len(nums2))//2-1
            k2=k1+1
        else:
            k1 = (len(nums1) + len(nums2))//2
            k2 = k1
        i = 0
        j = 0
        last=0
        s=0.0
        while True:
            if j > len(nums2)-1:
                i+=1
                last = nums1[i-1]
            elif i > len(nums1)-1:
                j+=1
                last = nums2[j-1]
            elif nums1[i] < nums2[j]:
                i+=1
                last = nums1[i-1]
            else:
                j+=1
                last = nums2[j-1]
            if i+j-1 == k1: 
                s+=last
            if i+j-1 == k2:
                s+=last
                break
        return s/2
s = Solution()
a = s.findMedianSortedArrays([2,4],[1,3])
        