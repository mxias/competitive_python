# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:26:34 2022

@author: Valiakmetov-AA
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        r = ListNode()
        cur = r
        prev = None
        while True:
            tmp = []
            del_ix = []
            for i in range(len(lists)):
                tmp.append(lists[i].val)
                lists[i] = lists[i].next
                if lists[i] == None:
                    del_ix.append(i)
            for i in range(len(del_ix)-1,-1,-1):
                lists.pop(del_ix[i])            
            tmp.sort()
            for i in tmp:
                if cur == None:
                    cur = ListNode()
                    prev.next = cur
                cur.val = i
                prev = cur
                cur = cur.next
            if len(tmp) == 0:
                break
        return r
            
                
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(5)
l1.next = l2
l2.next = l3

m1 = ListNode(1)
m2 = ListNode(3)
m3 = ListNode(4)
m1.next = m2
m2.next = m3

p1 = ListNode(2)
p2 = ListNode(6)
p1.next = p2
lists = []

lists.append(l1)
lists.append(m1)
lists.append(p1)
s = Solution()
r = s.mergeKLists(lists)
