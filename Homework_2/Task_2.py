# Задача 2.
#
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

def get_num(message):
    while True:
        try:
            int(message)
            return int(message)
        except ValueError:
            message = input("Entered not a number. Try again: ")
            continue

    # Можно так:

    # def multiply_digits(num):
    #     multiply = 1
    #     result = []
    #     for i in range(1, num+1):
    #         multiply *= i
    #         result.append(multiply)
    #     return result

    # print(
    #     multiply_digits(
    #         get_num(
    #             input("Enter the number: ")
    #         )
    #     )
    # )

    # Или так:


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def factor_list():
    result = []
    n = get_num(input("Enter the number: "))
    for i in range(1, n + 1):
        result.append(factorial(i))
    return result


print(factor_list())
