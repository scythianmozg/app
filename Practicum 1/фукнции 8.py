def find_square_and_perim(side1, side2):
    square = side1 * side2
    perimeter = 2 * (side1 + side2)
    return square, perimeter


square, perimeter = find_square_and_perim(7, 3)
print(f'Площадь прямоугольника равна {square}, периметр прямоугольника равен {perimeter}.')