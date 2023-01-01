# передадим в программу данные
beaufort = 6  # сильный ветер
is_raining = False  # дождя нет
temperature = 16

if (not is_raining or beaufort <= 4) and temperature > 22:
    print('Идём гулять, на улице хорошо')
else:
    print('Сидим дома, читаем Практикум')