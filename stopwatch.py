import time

def timer():
    print("Таймер")
    duration = int(input("Введите количество секунд для отсчета: "))
    print(f"Таймер запущен на {duration} секунд.")
    
    for i in range(duration, 0, -1):
        print(f"{i} секунд(ы)", end='\r')
        time.sleep(1)
    
    print("Время вышло!")

def stopwatch():
    print("Секундомер")
    input("Нажмите Enter, чтобы начать.")
    start_time = time.time()
    input("Нажмите Enter, чтобы остановить.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время: {elapsed_time:.2f} секунд.")

choice = input("Выберите: (1) Таймер (2) Секундомер: ")
if choice == "1":
    timer()
elif choice == "2":
    stopwatch()
else:
    print("Неверный выбор.")
