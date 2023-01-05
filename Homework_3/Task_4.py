# Задача 4.
#
# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36


import random


def get_num(message=input("Enter the number: ")):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


def get_list(n):
    res = []
    for i in range(n):
        res.append(round(random.random() * 10, 2))
    print(res)
    return res


# def fract(list):
#     for i in range(len(list)):
#         list[i] = round(list[i] - int(list[i]), 2)
#     return list


def fract(list, i=0):
    return round(list[i] - int(list[i]), 2)


def get_max_min(list):
    max = fract(list)
    min = fract(list)
    for i in range(len(list)):
        if (fract(list, i)) > max:
            max = fract(list, i)
        elif (fract(list, i)) < min:
            min = fract(list, i)
    print("max = ", max)
    print("min = ", min)
    return max, min


def difference(tuple):
    dif = round(tuple[0] - tuple[1], 2)
    print("Difference = ", dif)
    return dif


difference(
    get_max_min(
        get_list(
            get_num()
        )
    )
)
