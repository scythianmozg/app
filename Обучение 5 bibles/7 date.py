import datetime as dt 

start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

# Дата и время посадки: 1961 год, 12 апреля, 10 часов, 55 минут
landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)

print(landing_time - start_time) 