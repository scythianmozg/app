flat = [
    5.55, 22.19, 7.78, 26.86, 5.55, 29.84, 22.19, 5.55, 16.85, 4.52, 7.78]

# len(flat) подсчитает количество элементов в списке flat
# Сохраним это значение в переменную rooms_num
rooms_num = len(flat)
room_size = 7.78
room_count = 0
for room in flat:
    if room == room_size:
        room_count = room_count + 1

# И напечатаем полученное значение
print('Всего комнат ', rooms_num)
print('Всего комнат размером:', room_count)