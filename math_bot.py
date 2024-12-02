import sympy as sp

def math_help():
    print("Привет! Я могу помочь с решением математических задач.")
    while True:
        question = input("Введите математическую задачу (или 'выход' для завершения): ")
        if question.lower() == "выход":
            print("До свидания!")
            break
        try:
            result = sp.sympify(question)
            print(f"Решение: {result}")
        except:
            print("Не могу решить эту задачу. Попробуйте переформулировать.")

math_help()
