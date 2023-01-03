english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer'
}

# Создаём новый элемент словаря через доступ по ключу
english['голова'] = 'head'
english_list_eng = set(english.values())
english_list_ru = set(english.keys())

for word in english_list_eng:
    print(word)