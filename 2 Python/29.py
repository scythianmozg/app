a = int(input())
if a == 0:
    print('зеленый')
elif 1 <= a < 10 and a % 2 == 1:
    print('красный')
elif 1 <= a <= 10 and a % 2 == 0:
    print('черный')
elif 11 <= a <= 18 and a % 2 == 1:
    print('черный')
elif 11 <= a <= 18 and a % 2 == 0:
    print('красный')
elif 19 <= a <= 28 and a % 2 == 1:
    print('красный')
elif 19 <= a <= 28 and a % 2 == 0:
    print('черный')
elif 29 <= a <= 36 and a % 2 == 1:
    print('черный')
elif 29 <= a <= 36 and a % 2 == 0:
    print('красный')
else:
    print('ошибка ввода')