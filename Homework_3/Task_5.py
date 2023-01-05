# Задача 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def get_num(message=input("Enter the number: ")):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


def negafib(num):
    a, b = 1, 1
    list = [0]
    for i in range(num):
        list.append(a)
        list.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return list


print(negafib(get_num()))
