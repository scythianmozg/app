friends =  {
    'Серёга': 'Оренбург',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
dict_values = friends.values()
city_list = set(dict_values)

for city in city_list:
    print(city)
# Здесь ваш код