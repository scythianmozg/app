from math import *
n = int(input())

sum = 0
for i in range(1, n +1):
    num = 1/i
    sum += num
print(sum - log(n))