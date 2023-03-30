a = int(input())
b = int(input())

if a =='красный' and b =='синий':
    print('фиолетовый')
elif a =='синий' and b == 'желтый':
    print('зеленый')
elif a =='красный ' and b == 'желтый':
    print('оранжевый')
else:
    print('ошибка цвета')