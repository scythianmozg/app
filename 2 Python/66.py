total = 0
for i in range(5):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)