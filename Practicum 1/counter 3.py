movies_table = [
    ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
    ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
    ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
    ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
    ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
    ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
    ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
    ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
    ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
    ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
    ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
]

action_timing_total = 0 # переменная-счётчик для суммы

for movie in movies_table: # проходитесь по всем фильмам
    if 'боевик' in movie[3]: # если в столбце с жанрами (movie[3]) есть подстрока 'боевик',
        action_timing_total += movie[4] # то добавляете к счётчику продолжительность текущего фильма (movie[4])

print(action_timing_total)