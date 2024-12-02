import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Введите длину пароля: "))
    if length > 0:
        print(f"Ваш пароль: {generate_password(length)}")
    else:
        print("Длина пароля должна быть положительным числом.")
except ValueError:
    print("Введите корректное число!")
