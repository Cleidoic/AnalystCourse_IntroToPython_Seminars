# Задача 2.
#
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

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
        res.append(round(random.random() * 10))
    print(res)
    return res


def multiply(list):
    res = []
    for i in range((len(list)) // 2):
        res.append(list[i] * list[len(list) - i - 1])
    if len(list) % 2:
        res.append(list[len(list) // 2])
    return res


print(multiply(get_list(get_num())))
