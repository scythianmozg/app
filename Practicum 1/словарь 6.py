from json import dumps # подключение dumps() для красивого вывода словаря

movies_table = [
    {'movie_name':'Побег из Шоушенка', 'country':'США', 'genre':'драма', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'Крёстный отец', 'country':'США', 'genre':'драма, криминал', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'Тёмный рыцарь', 'country':'США', 'genre':'фантастика, боевик, триллер', 'year':2008, 'duration':152, 'rating':8.499}
]

print(dumps(movies_table, indent=4, ensure_ascii=False))