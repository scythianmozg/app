import pandas as pd

# подготавливаем данные и названия столбцов

atlas = [
    ['Франция','Париж'],
    ['Россия','Москва'],
    ['Китай','Пекин'],
    ['Мексика','Мехико'],
    ['Египет','Каир'],
]
geography = ['country', 'capital']

# создаём таблицу

world_map = pd.DataFrame(data=atlas , columns=geography) # создаём таблицу и сохраняем её в переменную world_map

print(world_map) # выводим таблицу на экран 