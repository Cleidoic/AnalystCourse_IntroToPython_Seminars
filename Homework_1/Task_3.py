# Задача 3:
#
# Напишите программу, которая принимает на вход
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
#
# *Пример:*
#
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3


def get_num(message):
    while True:
        try:
            int(message)
            1 / int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a digit or equal to zero. Try again: ")
            continue
        except ZeroDivisionError:
            message = input("Entered not a digit or equal to zero. Try again: ")
            continue


def define_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 > y:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


x = get_num(input("Entered X coordinate: "))
y = get_num(input("Entered Y coordinate: "))
print("Coordinate quarter number:", define_quarter(x, y))
