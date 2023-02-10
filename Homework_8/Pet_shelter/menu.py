from check_er import check
from db_actions import *
from db_impexp import *

add_dict = {"id": "1", "name": "", "breed": "", "aviary": "", "description": "", "sex": ""}


def menu():
    while True:
        read_all()
        print(f"\nPets book\n{'*' * 20}")
        actions = input("1. Show all entries\n"
                        "2. Find an entry\n"
                        "3. Add an entry\n"
                        "4. Edit an entry\n"
                        "5. Delete an entry\n"
                        "6. Import/Export\n"
                        "7. Exit\n")
        match actions:
            case "1":
                print_all()
            case "2":
                find_entry(input("Enter parameter value: "), read_all())
            case "3":
                add_entry(add_menu())
            case "4":
                print_all()
                id_change = input(f"Enter the id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                del_entry(input("Enter param value: "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Stop program.\n")
                print("Goodbye! See you soon sun!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def add_menu():
    logging.info('Start add menu')

    for i in add_dict:
        if i != "id":
            add_dict[i] = check(i)
    logging.info('Stop edit menu')
    return add_dict


def edit_menu():
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. name\n"
                       "2. breed\n"
                       "3. aviary\n"
                       "4. description\n"
                       "5. sex\n"
                       "6. exit\n")

        match change:
            case "1" | "2" | "3" | "4" | "5":
                type_date = add_dict[change]
                return type_date, check(type_date)
            case "6":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nImport\\Export:")
        change = input("1. import file\n"
                       "2. export file\n"
                       "3. exit\n")
        match change:
            case "1":
                file_import(input(f"Enter the database name: "))
                return
            case "2":
                while True:
                    logging.info('Start choose a format menu')
                    format_type = input(f"Choose a format:\n"
                                        f"1. CSV\n"
                                        f"2. JSON\n"
                                        f"3. XML\n"
                                        f"4. exit\n")
                    match format_type:
                        case "1":
                            save_csv(input("Enter the name of the file: "))
                            return
                        case "2":
                            save_json(input("Enter the name of the file: "))
                            return
                        case "3":
                            save_xml(input("Enter the name of the file: "))
                            return
                        case "4":
                            logging.info('Exited the choose a format menu')
                            return
                        case _:
                            logging.warning(f"Choose a format menu, wrong item selected.")
                            print("The data is not recognized, repeat the input.")

            case "3":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")
