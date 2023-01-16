english = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer'
}
# Собираем ключи словаря в коллекцию
# и преобразуем эту коллекцию в список
words_ru = list(english.keys())

# Собираем значения словаря в коллекцию
# и преобразуем эту коллекцию в список
words_en = list(english.values())

# Печатаем списки
print(words_ru)

print(words_en)

print(set(english.values()))
print(list((english.keys())))