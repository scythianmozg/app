flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

room_size = 7.78
count = 0

for room in flat:
    if room == room_size:
        count = count + 1

print('Комнат площадью', room_size, 'кв.м:', count)