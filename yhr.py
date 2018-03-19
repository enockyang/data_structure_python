##递归函数测试 recursive
import time
start = time.clock()

def abc(n):
  if (n < 2):
      return 1
  else:
      z = abc(n-1) + abc(n-2)
      return z

m = input('the number you want:  ')
print(abc(int(m)))

elapsed = (time.clock() - start)
print("Time used:",elapsed)