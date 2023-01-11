one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

# А без применения f-строк тот же код выглядит похуже:
print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.')