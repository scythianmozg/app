poem_str = 'Дама сдавала багаж'

# Применяем к строке метод split(), в скобках указываем пробел в кавычках:
words_list = poem_str.split(' ')
word_list_2 = poem_str.split()
# Печатаем результат:
print(word_list_2)

if 'Дама' in word_list_2:
    print('Д..а')
elif 'сдавала' in word_list_2:
    print('Сдала')
else:
    print('Б...')