import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    # Напишите тело этой функции.
    # Не изменяйте остальной код!
    try:
        request = requests.get(make_url(city), params=make_parameters())
        #print(request.status_code)
        if request.status_code == 200: return request.text
        else: return '<ошибка на сервере погоды>'
    except requests.ConnectionError : return '<сетевая ошибка>'

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
