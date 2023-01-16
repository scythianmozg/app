import requests

url = 'http://wttr.in/?0T'

response = requests.get('http://wttr.in/?0T')  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа