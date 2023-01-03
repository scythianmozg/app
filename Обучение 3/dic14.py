english = {
    'рука': 'hand',
	'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
	'бэкенд-разработчик': 'back-end developer'
}

# Элементу с ключом 'рука' присвоим новое значение
english['рука'] = 'arm'
english['рука'] = 'duck'

print(english.values())
print(english.keys())
word_ru = list(english.values())
print(word_ru)