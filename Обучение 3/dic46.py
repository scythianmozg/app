DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей - 
        # переберите словарь DATABASE в цикле
        for i in DATABASE:
            friends_string += i + ' '     
        # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string 
        return('Твои друзья: ' + friends_string) 
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'
# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))