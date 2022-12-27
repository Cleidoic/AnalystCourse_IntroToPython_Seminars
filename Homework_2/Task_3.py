# Задача 3.
#
# Задайте список из n чисел, заполненный
# по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#
# in
# 6
#
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

def get_num(message):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


n = get_num(input("Enter the number: "))


def list_numbers(n):
    result = []
    for i in range(1, n + 1):
        result.append(round(((1 + 1 / i) ** i), 3))
    return result


arr = list_numbers(n)
print(arr)


def sum_elements(list):
    result = 0
    for i in list:
        result += i
    return result


print(sum_elements(arr))
