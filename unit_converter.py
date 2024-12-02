def unit_converter():
    print("Конвертер единиц измерения")
    print("1. Конвертировать километры в метры")
    print("2. Конвертировать метры в километры")
    choice = input("Выберите действие: ")

    if choice == '1':
        km = float(input("Введите количество километров: "))
        print(f"{km} км = {km * 1000} м")
    elif choice == '2':
        meters = float(input("Введите количество метров: "))
        print(f"{meters} м = {meters / 1000} км")
    else:
        print("Неверный выбор!")

unit_converter()
