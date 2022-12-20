# Задание 1:
#
# Напишите программу, которая принимает на вход
# цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# 6 -> да
# 7 -> да
# 1 -> нет


def day_of_week():
    day = input("Enter the day of the week from 1 to 7: ")
    while not day.isdigit() or not 0 < int(day) < 8:
        day = input("Entered not a digit or not from 1 to 7. Try again: ")
    if 0 < int(day) < 6:
        print("No. Today is a weekday")
    else:
        print("Yes! Today is a weekend")


day_of_week()
