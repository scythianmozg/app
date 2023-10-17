# объявляем функцию
def multiplication(first_number, second_number, message='Результат умножения:', show_message=True): 
    result = first_number * second_number
    
    if show_message == True:
        print(message)

    print(result)

# Отключаем текстовое сообщение, меняя значение show_message на False
multiplication(2, 2, show_message=False)