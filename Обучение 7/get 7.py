import requests

request_headers = {
    'Accept-Language': 'en'  # попросим материал на английском языке
}
# сходим почитать блоги про IT
response = requests.get('https://habr.com/', headers=request_headers)
print(response.text)