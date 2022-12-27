from import_data import import_data
from export import export
from print import print
from search import search

def greeting():
    print("Здравствуйте. Вы вошли в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные действия с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите нужную цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export()
        print(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export()
        item = search(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(15), "Категория".center(30))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данные не обнаружены")