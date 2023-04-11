n = int(input())
largest = 0
second_largest = 0

for i in range(n):
    m = int(input())
    if m >= largest:
        second_largest = largest
        largest = m
    elif m > second_largest:
        second_largest = m
        
print(largest)
print(second_largest)