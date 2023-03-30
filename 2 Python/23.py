a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print(b)
elif c > b > a:
    print(b)
elif c > a > b:
    print(a)
elif b > a > c:
    print(a)
elif a > c > b:
    print(c)
else:
    print(c)
