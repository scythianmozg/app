#10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, поехали!
count = ''

for i in reversed(range(0, 11)):
    count = count + str(i) + ', '

print(count + 'поехали!')