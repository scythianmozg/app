string = 'По Борнео и Ямайке ходит слон в трусах и майке'
monument_string = 'Я памятник себе воздвиг нерукотворный'
index_list_str = [0, 1, 2, 8, 6, 17, 24]
index_list_monument = [0, 1, 2, 8, 6, 17, 24]

new_list = list(string)
new_set = set(string)

for i in index_list_monument:
    # На каждой итерации цикла 
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])

for i in index_list_str:
    # На каждой итерации цикла 
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(string[])