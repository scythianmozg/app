import datetime as dt

# Время, за которое Боттас сделал круг — это не дата, 
# а продолжительность, промежуток времени. Создаём данные типа timedelta:
time_bottas = dt.timedelta(minutes=1, seconds=25, microseconds=273250)

# Вычисляем timedelta Хэмилтона:
time_hamilton = time_bottas + dt.timedelta(microseconds = 208860)

print(time_hamilton)