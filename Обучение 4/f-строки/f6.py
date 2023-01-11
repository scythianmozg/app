def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    count = len(listened)
    return f'Вы прослушали {count} песен.'

def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
    T = 0
    for i in range (len(listened)):
        T+= int (listened[i])
    return (f'Вы прослушали {len(listened)} песен общей продолжительностью {T//60} минут.')  # напишите код функции calc_stat

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))