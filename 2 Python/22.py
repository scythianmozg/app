a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("Равносторонний")
elif a == b or a == c or c == b:
    print('Равнобедренный')
elif a != b != c:
    print('Разносторонний')
else:
    print('Другой')