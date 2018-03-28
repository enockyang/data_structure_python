# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:02:09 2018

@author: enock
"""
# check the (i,j) is in the matrix index
def isInside1(row,col,i,j):
    return (i in range(row)) and (j in range(col))

# get the max step from the current point
#def currentMaxStep(data,row,col,i,j):
#    max_step = 0
#    judge = 0
#    directs = [(-1,0),(1,0),(0,-1),(0,1)]
#    for (dx,dy) in directs:
#        x,y = i+dx,j+dy
#        if(isInside(row,col,x,y) and data[x][y] < data[i][j]):
#            judge = judge + 1
#    if judge == 0:
#        return max_step + 1
#    else:
#        for (dx,dy) in directs:
#            x,y = i+dx,j+dy
#            if(isInside(row,col,x,y) and data[x][y] < data[i][j]):
#                max_step = max(currentMaxStep(data,row,col,x,y),max_step)   
#        return max_step + 1
#better one
def currentMaxStep1(data,row,col,i,j):
    max_step=0
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    for (dx,dy) in directs:
        x,y = i+dx,j+dy
        if(isInside1(row,col,x,y) and data[x][y] < data[i][j]):
            max_step = max([currentMaxStep1(data,row,col,x,y),max_step])
    return max_step + 1
            

# traverse the whole data and generate the max step map
def getMaxMap1(data,row,col):
    import time
    start = time.clock()
    for i in range(1,10000):    
        Map = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                Map[i][j] = currentMaxStep1(data,row,col,i,j)
    elapsed = (time.clock() - start)
    print("Time used:",elapsed)
    print('the max step map is:')    
    for i in range(row):
        print(Map[i])
    return Map

# find the max from the max step map
def maxStep1(data,row,col):
    Map = getMaxMap1(data,row,col)
    return max([max(i) for i in Map])
            
    