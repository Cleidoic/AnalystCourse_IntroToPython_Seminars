# Задача 5
#
# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
#
# in
# 3
# 6
# 2
# 1
#
# out
# 5.099

def get_num(message):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 3)


x1 = get_num(input("Enter the x coordinate of the first point: "))
y1 = get_num(input("Enter the y coordinate of the first point: "))
x2 = get_num(input("Enter the x coordinate of the second point: "))
y2 = get_num(input("Enter the y coordinate of the second point: "))

print(get_distance(x1, y1, x2, y2))
