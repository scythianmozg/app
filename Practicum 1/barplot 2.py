import matplotlib
import seaborn
import pandas

matplotlib.rcParams['figure.figsize'] = [15, 7] # указываем размер графика

months = pandas.Series(['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'])

games_released = pandas.Series([503, 588, 689, 697, 711, 658,
                  709, 716, 720, 745, 723, 701])

seaborn.barplot(x=months, y=games_released)