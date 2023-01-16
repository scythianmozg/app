user_query = 'как стать бэкенд-разработчиком'
user_querry = user_query.replace(' ', '%20')
url = 'https://yandex.ru/search/?text=' + user_querry + str('&lr=213')
 
print(url)