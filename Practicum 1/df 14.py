def replace_wrong_values(wrong_values, correct_value): # на вход функции подаются список неправильных значений и строка с правильным значением
    for wrong_value in wrong_values: # перебираем неправильные имена
        tennis['name'] = tennis['name'].replace(wrong_value, correct_value) # и для каждого неправильного имени вызываем метод replace()

duplicates = ['Roger Fderer', 'Roger Fdrer', 'Roger Federer'] # список неправильных имён
name = 'Роджер Федерер' # правильное имя
replace_wrong_values(duplicates, name) # вызов функции, replace() внутри будет вызван 3 раза
print(tennis) # датафрейм изменился, неявные дубликаты устранены