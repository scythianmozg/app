n = int(input())

counter = 0
sum = 0
for i in range(1, n+1):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        sum += i
print(sum)