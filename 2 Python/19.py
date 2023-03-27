x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('YES')
else:
    print('NO')