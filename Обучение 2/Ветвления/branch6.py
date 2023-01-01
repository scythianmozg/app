for messages_count in range(6):
    if messages_count > 0:
        print('Новых сообщений: ' + str(messages_count))
    else:
        print('У вас нет сообщений')

for current_hour in range(2):
    if  current_hour < 12:
        print('Доброе утро!')