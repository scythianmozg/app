import datetime as dt

# Как и раньше - определяем текущее время UTC
utc_time = dt.datetime.utcnow()

# Создаём промежуток времени в три часа
period = dt.timedelta(minutes=30*6)

# И прибавляем к значению времени по UTC поправку в три часа:
moscow_time = utc_time + period

# Печатаем
print(moscow_time) 