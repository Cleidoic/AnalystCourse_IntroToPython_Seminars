# Задача 1.
#
# Напишите программу, которая принимает
# на вход вещественное число и показывает сумму
# его цифр. Без работы с методами строк.
#
# in -> out
#
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

def get_num(message):
    while True:
        try:
            float(message)
            return float(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue


def sum_digit(num):
    sum = 0
    while num % 10 != 0:
        num *= 10
    while num != 0:
        sum += num % 10
        num //= 10
    return int(sum)


print(
    sum_digit(
        get_num(
            input("Enter the number whose sum of digits you want to calculate: "))
    )
)
