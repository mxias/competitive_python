# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:23:17 2022

@author: Valiakmetov-AA
"""
import math
class FindThePerfectTriangle:
    @staticmethod 
    def search_coord(pos_dif1, pos_dif2, pos_dif3, C):
        for (X21, Y21) in pos_dif1:
            for (X31, Y31) in pos_dif2:
                for (X32, Y32) in pos_dif3:
                    if X21+X31+X32==0 and Y21+Y31+Y32==0 and (X21 + X31) **2 + (Y21 + Y31)**2 == C**2: 
                        return [0, 0, X21, Y21, X21 + X31, Y21 + Y31]
        return []
    @staticmethod
    def normalize(coords):
        minx = 0;
        miny = 0;
        for i in range(len(coords)):
            if i%2 == 0 and miny > coords[i]:
                miny = coords[i]
            elif i%2 != 0 and minx > coords[i]:
                minx = coords[i]
        for i in range(len(coords)):
            if i%2 == 0:
                coords[i] -= miny
            else:
                coords[i] -= minx    
            
        return [it + 1 for it in coords]
            
    @staticmethod 
    def square(a,b,c):
        p = 0.5*(a+b+c)
        S = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return S
    @staticmethod 
    def two_squares(N):
        pos_dif = []
        for i in range(0, math.floor(math.sqrt(N/2))+1):
            m = math.sqrt(N - i*i)
            if int(m) == m:
                m = int(m)
                X_s = m**2 - i**2
                Y_s = 2*m*i
                pos_dif.append((X_s, Y_s))
                pos_dif.append((-X_s, Y_s))
                pos_dif.append((X_s, -Y_s))
                pos_dif.append((-X_s, -Y_s))
                pos_dif.append((Y_s, X_s))
                pos_dif.append((-Y_s, X_s))
                pos_dif.append((Y_s, -X_s))
                pos_dif.append((-Y_s, -X_s))
        pos_dif.append((0, N))
        pos_dif.append((0, -N))
        pos_dif.append((N, 0))
        pos_dif.append((-N, 0))
        return pos_dif

    @staticmethod
    def constructTriangle(s, p):
        begin = p//2
        if begin == p/2:
            begin-=1
        for A in range(begin, math.ceil(p/3)-1, -1):
            pos_dif1 = FindThePerfectTriangle.two_squares(A)
            for B in range(A-1, 0, -1):
                C = p - A - B
                if not( A+B>C and A+C>B and B+C>A):
                    continue
                pos_dif2 = FindThePerfectTriangle.two_squares(B)
                pos_dif3 = FindThePerfectTriangle.two_squares(C)
                if FindThePerfectTriangle.square(A,B,C) != s:
                    continue
                coords = FindThePerfectTriangle.search_coord(pos_dif1, pos_dif2, pos_dif3, C)

                coords = FindThePerfectTriangle.normalize(coords)
                return coords 
        return []
a = FindThePerfectTriangle.constructTriangle(12, 18)       
        