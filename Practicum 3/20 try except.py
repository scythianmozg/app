position = [
    ['2019-05-01', '- 6'],
    ['2019-05-02', '+5'],
    ['2019-05-03', ' 5'],
    ['2019-05-04', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', 'Error 5'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]
count_lines = 0
total_position = 0

for row in position:
    count_lines += 1
    level = int(row[1]) #в этой переменной сохраните позицию в выдаче 
    total_position += level #сложите все позиции в этой переменной
print(total_position/count_lines)