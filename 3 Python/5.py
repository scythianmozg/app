a = int(input())
b = int(input())

counter = 0
for i in range(a, b+1):
    if pow(i, 3) % 10 == 9 or pow(i, 3) % 10 == 4:
        counter += 1
print(counter)