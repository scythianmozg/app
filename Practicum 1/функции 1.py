first_item_price = 100.0 # цена первого продукта
first_item_number = 3 # его количество

second_item_price = 501.0 # цена второго продукта
second_item_number = 2 # его количество

third_item_price = 40.0 # цена третьего продукта
third_item_number = 10 # его количество

# находим общую стоимость первой позиции
first_item_total = first_item_number * first_item_price
if first_item_total > 1000: # если она превышает 1000,
    first_item_total -= first_item_total * 0.05 # то уменьшаем стоимость на пять процентов
print(first_item_total)

# находим общую стоимость второй позиции
second_item_total = second_item_number * second_item_price 
if second_item_total > 1000: # если она превышает 1000,
    second_item_total -= second_item_total * 0.05 # то уменьшаем стоимость на пять процентов
print(second_item_total)

# находим общую стоимость третьей позиции
third_item_total = third_item_number * third_item_price
if third_item_total > 1000: # если она превышает 1000,
    third_item_total -= third_item_total * 0.05 # то уменьшаем стоимость на пять процентов
print(third_item_total)