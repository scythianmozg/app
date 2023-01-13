# Подключите библиотеку random и дайте ей краткое имя
from random import choice as c

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    # Напишите ваш код здесь
    return c(answers)

print(how_are_you())