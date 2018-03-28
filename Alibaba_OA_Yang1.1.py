# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:46:02 2018

@author: enock
"""
N=1000

def phi(n):
    y = n
    #print(round(n**0.5)+1)
    for i in range(2,round(n**0.5)+1):
        if n % i  == 0 :
            y -= y/i
            while (n % i ==0):
                n /= i
        else:
            continue
    if (n>1):
        y -= y/n
    return int(y)

count = 3
new_points = 0

for i in range(2,N+1):
    new_points += phi(i)
    

S = count + 2*new_points 

print(S)
