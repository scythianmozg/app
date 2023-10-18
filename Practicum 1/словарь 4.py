monuments = [
    {
        'name': 'Статуя Единства', # название
        'country': 'Индия', # страна
        'height': 182 # высота без постамента
    },
    {
        'name': 'Статуя богини Каннон в Сендае',
        'country': 'Япония',
        'height': 100
    },
    {
        'name': 'Родина-Мать зовёт!',
        'country': 'Россия',
        'height': 85
    },
    {
        'name': 'Будда Дорденма',
        'country': 'Бутан',
        'height': 51.5
    },
    {
        'name': 'Статуя Свободы',
        'country': 'США',
        'height': 46
    }
]
height_total = 0 # переменная для общей суммы заказа

for item in monuments: # перебираете каждый словарь в списке
    height_total += item['height']

print(height_total/len(monuments))