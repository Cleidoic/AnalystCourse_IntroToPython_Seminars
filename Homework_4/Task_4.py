# Задача 4:
#
# Задана натуральная степень k.
# Сформировать случайным образом список
# коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен
# не менее 3-х раз.
#
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import choice, sample


def polynominal():
    num = int(input("Enter the number of coefficients: "))
    name = input("Enter the file name: ")

    for _ in range(4):

        if num < 1:
            return 0

        poly = ""
        num_list = range(0, 11)

        with open(name, "a", encoding="utf-8") as my_f:

            for i in range(num, 1, -1):

                value = choice(num_list)
                if value:
                    poly += f"{value}*x^{i} {choice('+-')} "

            numbers = sample(range(1, 11), k=2)
            my_f.write(f"{poly}{choice(numbers)}*x {choice('+-')} {choice(numbers)} = 0\n")
    return name

# polynominal()
