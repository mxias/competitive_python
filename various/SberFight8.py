# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 00:03:53 2022

@author: Valiakmetov-AA
"""

from collections import defaultdict 
 
class Solution: 
	 
	def countCycle(self, n, pairs): 
		self.graph=defaultdict(list) 
		self.visited=defaultdict(lambda: 0) 
		self.count=0 
		for var1, var2 in pairs: 
			self.addEdge(var1,var2) 
 
		for i in range(n): 
			self.depthFirstSearch(i) 
 
		return self.count 
 
	def addEdge(self, var1, var2): 
		self.graph[var1].append(var2) 
 
	def depthFirstSearch(self,var): 
		#if cycle is detected 
		if self.visited[var]==-1: 
			self.count+=1 
			return  
		#if depth first search has been completed on this variable 
		if self.visited[var]==1: 
			return  
 
		self.visited[var]=-1 
 
		for neighb in self.graph[var]: 
			self.depthFirstSearch(neighb) 
	 
		#mark depth first search on this variable as completed 
		self.visited[var]=1 
 
 
 

def get_result(deal):
    g =[] 
    for i in deal:
        begin = ord(i[0])-97
        index = i.find('-')
        if index != -1:
            for j in i[index+1:]:
                g.append((begin, ord(j)-97))
    s = Solution()
    num=s.countCycle(len(deal),g) 
    return num

deal = ["a-b", "b-c", "c-a"]
a = get_result(deal)