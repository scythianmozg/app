a, b, c, d = int(input()), int(input()), int(input()), int(input())
min1 = 0
min2 = 0
min3 = 0
if a > b:
    min1 = b
else:
    min1 = a
if c > d:
    min2 = d
else:
    min2 = c
if min1 > min2:
    min3 = min2
else:
    min3 = min1
print(min3)