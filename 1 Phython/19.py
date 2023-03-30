num = int(input())
digit1 = (num % 10) // 1
digit2 = (num % 100) // 10
digit3 = (num % 1000) // 100
digit4 = (num % 10000) // 1000

print('Цифра в позиции тысяч равна', digit4)
print('Цифра в позиции сотен равна', digit3)
print('Цифра в позиции десятков равна', digit2)
print('Цифра в позиции единиц равна', digit1)