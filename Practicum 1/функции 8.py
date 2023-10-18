nba_players = {
    'Джеймс Харден': [2191, 2818, 2335],
    'Леброн Джеймс': [2251, 1505, 1698],
    'Дэмиан Лиллард': [1962, 2067, 2009],
}

for player, digits in nba_players.items():
    average = int(sum(digits))/len(digits)
    print(f'{player} {int(average)}')