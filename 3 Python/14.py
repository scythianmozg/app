counter = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        counter = counter + 1
if counter == 10:
    print('YES')
else:
    print('NO')