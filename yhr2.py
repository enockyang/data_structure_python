##两种算多项式值的算法好坏比较
import time

def method1(n,a,x):
    p = a[0]
    for i in range(1,n+1):
        p +=  (a[i]*pow(x,i))
    return p

def method2(n,a,x):
    p = a[n]
    for i in range(1,n+1):
        i1 = n+1-i
        p = (a[i1-1] + x*p)
    return p

n = input('the number you want:  ')
n = int(n)
a = range(1,n+2)
x = 10

start = time.clock()
answer1 = method1(n,a,x)
elapsed = (time.clock() - start)

start2 = time.clock()
answer2 = method2(n,a,x)
elapsed2 = (time.clock() - start2)

print('answer1: ',answer1)
print('time used',elapsed)
print('answer2: ',answer2)
print('time used2',elapsed2)



