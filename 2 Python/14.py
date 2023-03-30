num = int(input())
digit1 = (num % 10) // 1
digit2 = (num % 100) // 10
digit3 = (num % 1000) // 100
digit4 = (num % 10000) // 1000
if digit1 != digit2 and digit1 != digit3 and digit2 != digit3:
    print('Все цифры разные')
else:
    print('Есть одинаковые цифры')