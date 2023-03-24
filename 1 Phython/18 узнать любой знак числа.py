num = int(input())
digit1 = (num % 10) // 1
digit2 = (num % 100) // 10
digit3 = (num % 1000) // 100
digit4 = (num % 10000) // 1000

print(digit1 + digit2 + digit3 + digit4)