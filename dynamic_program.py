# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:26:22 2018

@author: enock
"""
N=5
def gcd(x,y):
    if x%y == 0:
        return y
    return gcd(y,x%y)

count = 3
for i in range(2,N+1):
    new_points = 0
    for j in range(1,i):
        if gcd(i,j) == 1:
            new_points = new_points + 1
    count = count + 2*new_points

S = count

print(S)

        
        
        