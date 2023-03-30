num = int(input())
x1 = (num % 10) // 1
x2 = (num % 100) // 10
x3 = (num % 1000) // 100
if (x1 + x2 + x3 == 2*max(x1, x2, x3)):
    print('Число интересное')
else:
    print('Число неинтересное')