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
        filtered_order.append(item) # ...то добавим словарь в список filtered_order

print(filtered_order) # печатаем отфильтрованный список словарей