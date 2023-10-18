order = [
    {
        'item': 'Пицца Маргарита', # название позиции
        'category': 'пицца', # категория товара
        'quantity': 2, # количество в заказе
        'comment': 'Побольше сыра, пожалуйста!', # комментарий к заказу
        'price': 320 # стоимость одной единицы товара
    },
    {
        'item': 'Пицца с ветчиной',
        'category': 'пицца',
        'quantity': 1,
        'comment': '',
        'price': 410
    },
    {
        'item': 'Pepsi 1 л',
        'category': 'напитки',
        'quantity': 3,
        'comment': '',
        'price': 75
    },
    {
        'item': 'Сок яблочный 0.5 л',
        'category': 'напитки',
        'quantity': 1,
        'comment': '',
        'price': 80
    },
    {
        'item': 'Круассан с сыром',
        'category': 'выпечка',
        'quantity': 2,
        'comment': '',
        'price': 130
    }
]

total_price = 0
for item in order:
    if item['category'] == 'пицца':
        total_price += item['price']
print(total_price)