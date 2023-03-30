num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Сумма цифр =', digit3 + digit2 + digit1)
print('Произведение цифр =', digit3 * digit2 * digit1)