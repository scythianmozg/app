m = int(input())
n = int(input())

for i in range(m, n+1):
    if i % 17 == 0 or i % 15 == 0 or i % 10 == 9:
        print(i)


n = int(input())
for i in range(1, 11):
    print(n,"x", i, "=", n*i )