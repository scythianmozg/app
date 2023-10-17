order = [
    {
        'item': 'Пицца Маргарита', # название позиции
        'category': 'пицца', # категория товара
        'quantity': 2, # количество в заказе
        'price': 320 # стоимость
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

total_price = 0 # переменная для общей суммы заказа

for item in order: # перебираете каждый словарь в списке
    total_price += item['price'] * item['quantity'] # добавляете к переменной стоимость товара, умноженную на количество

print(total_price)