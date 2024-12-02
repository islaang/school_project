import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Угадайте число от 1 до 100: ")
        attempts += 1
        if not guess.isdigit():
            print("Введите число!")
            continue
        guess = int(guess)
        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток.")
            break

guess_the_number()