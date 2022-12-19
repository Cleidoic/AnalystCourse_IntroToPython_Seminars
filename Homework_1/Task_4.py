# Задача 4
#
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#
# *Пример:*
#
# 1 -> x > 0, y > 0
# 8 -> нет такой четверти

def get_num(message):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a digit. Try again: ")
            continue


def get_range(quarter):
    match quarter:
        case 1:
            print("Range: x > 0 and y > 0")
        case 2:
            print("Range: x < 0 and y > 0")
        case 3:
            print("Range: x < 0 and y < 0")
        case 4:
            print("Range: x > 0 and y < 0")
        case _:
            print("No such range")


quarter = get_num(input("Enter the number of the coordinate quarter from 1 to 4: "))
get_range(quarter)
