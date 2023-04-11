num = int(input())
largest = 0
smallest = 9

while num != 0:
    last_digit = num % 10
    if last_digit > largest:
        largest = last_digit
    if last_digit < smallest:
        smallest = last_digit
    num = num // 10
print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)