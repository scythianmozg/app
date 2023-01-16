import requests

search_parameters = {
    'text': 'что такое backend',
    'lr': 213
}
url = 'https://yandex.ru/search/'
# Функция get() приняла на вход URL и параметры поиска,
# а дальше она знает, что делать
response = requests.get(url, params=search_parameters)

print(response.status_code)
print(response.url)