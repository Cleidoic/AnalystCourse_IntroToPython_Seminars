# Задача 5.
#
# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
#
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

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
        res.append(i)
    return res


# def shuffle():


print(get_list(get_num(input())))
