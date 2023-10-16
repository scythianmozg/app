# в заголовок добавляем значение по умолчанию для eggs_number
def omelet(eggs_number=2):
    result = 'Омлет готов! Яиц в омлете: ' + str(eggs_number)
    return result

print(omelet())