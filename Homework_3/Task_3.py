# Задача 3.
#
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк
#
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

def get_num(message=input("Enter the number: ")):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


def bin_convert(n):
    res = []
    while n:
        res.insert(0, n % 2)
        n //= 2
    return res


print(*bin_convert(get_num()), sep='')
