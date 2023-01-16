import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '1': '',
    'T': '',# добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'M': '',
    'lang': 'ru'
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)