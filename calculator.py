def calculator():
    print("Простой калькулятор. Введите 'выход', чтобы завершить.")
    while True:
        operation = input("Выберите операцию (+, -, *, /): ")
        if operation == "выход":
            break
        if operation not in ["+", "-", "*", "/"]:
            print("Неправильная операция, попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if operation == "+":
                print(f"Результат: {num1 + num2}")
            elif operation == "-":
                print(f"Результат: {num1 - num2}")
            elif operation == "*":
                print(f"Результат: {num1 * num2}")
            elif operation == "/":
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(f"Результат: {num1 / num2}")
        except ValueError:
            print("Введите корректные числа!")

calculator()
