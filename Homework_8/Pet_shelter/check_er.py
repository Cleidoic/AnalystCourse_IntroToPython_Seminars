import logging


def find_entry(data_find, all_info):
    logging.info(f"Search for an entry: {data_find}")
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        logging.info(f"Search result: {candidates}")
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Name or aviary not found.\n")
        return 0


def matching_rec(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def check(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "name breed description":
            if answer.isalpha():
                return answer
            else:
                answer = input(f"Data is incorrect!\n"
                           f"Use only the letters"
                           f" of the alphabet, the length\n"
                           f"Enter a {num}: ")
        else:
            return answer
