nba_players = {
    'Джеймс Харден': [2191, 2818, 2335],
    'Леброн Джеймс': [2251, 1505, 1698],
    'Дэмиан Лиллард': [1962, 2067, 2009],
}


nba_total_1 = 0 # переменная для общей суммы заказа

for i in nba_players.get('Джеймс Харден'):
    nba_total_1 += i
print(int(nba_total_1/len(nba_players)))

nba_total_2 = 0 # переменная для общей суммы заказа

for i in nba_players.get('Леброн Джеймс'):
    nba_total_2 += i
print(int(nba_total_2/len(nba_players)))

nba_total_3 = 0
for i in nba_players.get('Дэмиан Лиллард'):
    nba_total_3 += i
print(int(nba_total_3/len(nba_players)))