# Задача 1.
#
# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
# out
# [4, 2, 4, 9]
# 8

import random

def get_num(message):
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
        res.append(round(random.random()*100))
    print(res)
    return res


def sum_odd(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    return sum


print(sum_odd(get_list(get_num(input("Enter the number: ")))))
