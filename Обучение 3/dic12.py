english = {
    'рука': 'hand', # Первый элемент словаря (да, в каждом элементе две части!)
    'нога': 'leg',  # Второй элемент словаря
    'хвост': 'tail',  # Третий элемент
    'питон': 'python',  # Четвёртый элемент
    'бэкенд-разработчик': 'back-end developer',  # Пятый элемент
    'medical': 'медицинский',
} 

dump = {
    1: 'единица',               # Ключ - число, значение - строка.
    'земляника': 'ягода',       # И ключ, и значение - строки.
    'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
    False: 0,                   # Ключ - булево значение, значение - число.
    'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
                                # Ключ - строка, а значение - словарь. Так тоже можно!
    'англо-русский словарь': {'рука': 'hand', 
                              'нога': 'leg', 
                              'бэкенд-разработчик': 'back-end developer'
                               },    
}
print(english['рука'])
print(english['medical'])
print(english['лук'])