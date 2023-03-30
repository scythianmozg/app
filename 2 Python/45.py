name1 = input()
name2 = input()
name3 = input()
lengh1 = int(len(name1))
lengh2 = int(len(name2))
lengh3 = int(len(name3))

len_max = max(lengh1, lengh2, lengh3)
len_min = min(lengh1, lengh2, lengh3)

if len_min == lengh1:
    print(name1)
elif len_min == lengh2:
    print(name2)
else:
    print(name3)

if len_max == lengh1:
    print(name1)
elif len_max == lengh2:
    print(name2)
else:
    print(name3)