import os
import datetime

def habit_tracker():
    habit = input("Введите привычку для отслеживания: ")
    filename = "habit_tracker.txt"

    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("Дата, Выполнил ли привычку?\n")

    while True:
        answer = input(f"Выполнили ли вы привычку: '{habit}'? (да/нет): ").lower()
        if answer == "да":
            result = "Выполнил"
        elif answer == "нет":
            result = "Не выполнил"
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")
            continue

        date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(filename, 'a') as file:
            file.write(f"{date}, {result}\n")
        
        print(f"Записано: {date} - {result}")
        again = input("Хотите ввести еще раз? (да/нет): ").lower()
        if again != "да":
            break

habit_tracker()
