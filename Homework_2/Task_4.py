# Задача 4.
#
# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка,
# заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на
# указанных позициях(не индексах).
#
# Enter the value of N: 5
# Position one: 1
# Position two: 2
#
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

def get_num(message):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


n = get_num(input("Enter the number: "))


def get_list(n):
    result = []
    for i in range(-n, n + 1):
        result.append(i)
    return result


arr = get_list(n)
print(arr)


def multi_elements(p_1, p_2):
    return arr[p_1 - 1] * arr[p_2 - 1]


p_1 = get_num(input("Enter position one: "))
p_2 = get_num(input("Enter position two: "))
multi = multi_elements(p_1, p_2)
print(multi)
