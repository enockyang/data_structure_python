# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:26:22 2018

@author: enock
"""
N=2000
#Euclidean algorithm 辗转相除法版本
def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
    
count = 3
new_points = 0

for i in range(2,N+1):
    for j in range(1,i):
        if gcd(i,j) == 1:
            new_points += 1
    

S = count + 2*new_points 

print(S)

        
        
        