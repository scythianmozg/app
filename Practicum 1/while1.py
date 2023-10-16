from random import randint

capacity = 400 # грузоподъёмность лифта
total_weight = 0 # переменная для суммарного веса

while total_weight < capacity: # пока суммарный вес меньше грузоподъёмности лифта
    person_weight = randint(30, 120) # генерируется случайное целое число от 30 до 120
    total_weight += person_weight # сгенерированный вес добавляется к суммарному весу

print(f'А всё уже, всё уже! Лифт заполнен! Раньше надо было! Загруженность: {total_weight}')