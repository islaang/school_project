import random

options = ["Камень", "Ножницы", "Бумага"]

while True:
    user_choice = input("Выберите: Камень, Ножницы, Бумага (или 'выход' для завершения): ").capitalize()
    if user_choice == 'Выход':
        break
    if user_choice not in options:
        print("Неправильный ввод, попробуйте снова.")
        continue

    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
         (user_choice == "Бумага" and computer_choice == "Камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

