# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:57:37 2018

@author: enock
"""
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    def char2num(s):
        return DIGITS[s]
    def fn1(x,y):
        return x*10+y
    def fn2(x,y):
        return x*0.1+y
    for index,number in enumerate(s,0):
        if number == '.':
            a = index
    s1 = s[0:a] 
    s2 = s[a+1:len(s)]
    s3 = s2[::-1]
    s3 = s3 + '0'    
    return reduce(fn1, map(char2num,s1))+reduce(fn2, map(char2num,s3))    
    
print(str2float('123.456')) 
print(type(str2float('123.456')))   