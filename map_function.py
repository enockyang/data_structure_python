# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:09:49 2018

@author: enock
"""

##规范名字
def normalize(namelist):
    def norm(x):
        a = x[0].upper()
        for i in range(1,len(x)):
            a = a + x[i].lower()
        return a 
    return list(map(norm,namelist))

L1 = ['adam', 'LISA', 'barT']

print(normalize(L1))