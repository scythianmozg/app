from random import choice  # Импорт одной функции из библиотеки

def find_a_present(prizes):
    # Обращаемся к функции напрямую: choice(), а не random.choice()
    return choice(prizes) 

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))