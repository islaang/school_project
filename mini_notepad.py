def mini_notepad():
    print("Мини-блокнот")
    filename = input("Введите имя файла для сохранения заметок: ")

    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Закрыть блокнот")

        choice = input("Ваш выбор: ")

        if choice == '1':
            note = input("Введите вашу заметку: ")
            with open(filename, 'a') as file:
                file.write(note + '\n')
            print("Заметка добавлена!")
        elif choice == '2':
            try:
                with open(filename, 'r') as file:
                    notes = file.read()
                    print("Заметки:")
                    print(notes)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '3':
            print("Закрытие блокнота...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

mini_notepad()
