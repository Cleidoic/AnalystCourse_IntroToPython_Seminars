# Задача 3:
#
# Написать функцию, аргументы имена сотрудников,
# возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
#
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def thesaurus(*args):
    name_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in name_dict:
            name_dict[letter] = [i]
        else:
            name_dict[letter] += [i]

    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

# ------------- Вариант 2:

from itertools import groupby


def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


# ------------- Вариант 3:

def thesaurus(*args):
    if "" not in args:
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
