from json import dumps # подключение dumps() для красивого вывода списка словарей


order = [
    {
        'item': 'Пицца Маргарита',
        'category': 'пицца',
        'quantity': 2,
        'price': 320
    },
    {
        'item': 'Пицца с ветчиной',
        'category': 'пицца',
        'quantity': 1,
        'price': 410
    },
    {
        'item': 'Pepsi 1 л',
        'category': 'напитки',
        'quantity': 3,
        'price': 75
    }
]

filtered_order = [] # переменная для хранения результата

for item in order: # перебираем каждый словарь в списке
    if item['category'] == 'пицца': # если категория - пицца...
        filtered_order.append(item) # ...то добавим в словарь в список filtered_order

print('Результат:')
print(dumps(filtered_order, indent=4, ensure_ascii=False)) # печатаем список с помощью dumps()