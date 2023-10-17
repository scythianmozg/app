# объявляем функцию calculate_total_price с двумя параметрами: # price и count
def calculate_total_price(price, count): # заголовок функции: ключевое слово def, имя функции и формальные параметры в скобках
    total = price * count # в теле функции считаем стоимость позиции в корзине
    if total > 1000: # сравниваем стоимость с 1000 в условной конструкции
        total -= total * 0.05 # уменьшаем стоимость на 5%, если она больше 1000
    return total # возвращаем значение стоимости

first_item_count = 3
first_item_price = 100.0

second_item_count = 2
second_item_price = 501.0

third_item_count = 10
third_item_price = 40.0

# Трижды вызываем функции: 
# вместо price и count указываем аргументы,
# то есть фактическую цену и количество товара.
# Результат каждого вызова сохраняем в переменных.
first_item_total = calculate_total_price(first_item_price, first_item_count)
second_item_total = calculate_total_price(second_item_price, second_item_count)
third_item_total = calculate_total_price(third_item_price, third_item_count)

print(first_item_total)
print(second_item_total)
print(third_item_total)