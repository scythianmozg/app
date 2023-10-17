def is_age_appropriate_one(age, threshold): # передаём возраст и порог
    if age >= threshold: # если возраст больше или равен порогу, 
        return True # то возвращаем True
    return False # иначе возвращаем False

print(is_age_appropriate_one(17, 12))

def is_age_appropriate_two(age, threshold):
    return age >= threshold # вернёт True или False

print(is_age_appropriate_two(17, 12))