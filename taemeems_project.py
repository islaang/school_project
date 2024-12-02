# -*- coding: UTF-8 -*-

import random

# Banner at the start
def print_banner():
    print("""
    .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------.  .--------------.  .--------------. || .--------------. |
    | |          |  |      _       |  |   _  _   | || |     ____     | |
    | |   |    |   |  |     / \\      |  |  |   \\/   |  |  |   / __ \\    | |
    | |    \\    /    |  |    / /\\ \\     |  |  | |\\  /| |  | || |  | |  | |   | |
    | |     \\  /     |  |   / ____ \\    |  |  | |_\\/_| |  | || |  | |__| |_  | |
    | |      \\/      |  | _/ /    \\ \\_  |  |  |___||___|  | || |   \\____\\__| | |
    | |              |  |              |  |              | || |              | |
    | '--------------'  '--------------'  '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------' 
    """)

print_banner()

# Function to select language
def select_language():
    print("Choose your language / Выберите язык / اختر لغتك:")
    print("1) English")
    print("2) Russian")
    print("3) Arabic")

    while True:
        language_choice = input("Type 1, 2, or 3 to select a language: ")
        if language_choice == '1':
            return 'english'
        elif language_choice == '2':
            return 'russian'
        elif language_choice == '3':
            return 'arabic'
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Translations for prompts and messages
translations = {
    'english': {
        'welcome': "Welcome to Yada's assistant!",
        'name_prompt': "What can I refer to you as?",
        'how_can_help': "How else can I help you?",
        'exit': "Goodbye! Have a great day!",
        'calculator': "Let's do some calculations.",
        'rps': "Welcome to Rock, Paper, Scissors! Choose one: r for rock, s for scissor, p for paper.",
        'quiz': "Let's begin the quiz!",
        'first_number': "Enter the first number: ",
        'second_number': "Enter the second number: ",
        'operator': "Choose an operator (+, -, /, *): ",
        'invalid_operator': "Invalid operator. Please choose one of +, -, /, *.",
        'invalid_choice': "Invalid choice. Please try again.",
        'help': "Use 'calculator', 'rps', or 'quiz' for respective functions, or type 'exit' to quit."
    },
    'russian': {
        'welcome': "Добро пожаловать в помощника Яды!",
        'name_prompt': "Как мне к вам обращаться?",
        'how_can_help': "Чем еще я могу вам помочь?",
        'exit': "До свидания! Хорошего дня!",
        'calculator': "Давайте сделаем несколько расчетов.",
        'rps': "Добро пожаловать в Камень, Ножницы, Бумага! Выберите: r для камня, s для ножниц, p для бумаги.",
        'quiz': "Давайте начнем викторину!",
        'first_number': "Введите первое число: ",
        'second_number': "Введите второе число: ",
        'operator': "Выберите оператора (+, -, /, *): ",
        'invalid_operator': "Неверный оператор. Пожалуйста, выберите один из +, -, /, *."
    },
    'arabic': {
        'welcome': "مرحبًا في مساعد يدى!",
        'name_prompt': "كيف يمكنني مناداتك؟",
        'how_can_help': "كيف يمكنني مساعدتك أكثر؟",
        'exit': "وداعًا! أتمنى لك يومًا سعيدًا!",
        'calculator': "لنقم ببعض الحسابات.",
        'rps': "مرحبًا في حجر، ورقة، مقص! اختر واحدًا: r للحجر، s للمقص، p للورقة.",
        'quiz': "لنبدأ الاختبار!",
        'first_number': "أدخل الرقم الأول: ",
        'second_number': "أدخل الرقم الثاني: ",
        'operator': "اختر عامل (+، -، /، *): ",
        'invalid_operator': "عامل غير صالح. يرجى اختيار واحد من +، -، /، *."
    }
}

select_language()

# Function to display message in selected language
def get_translation(language, key):
    return translations[language].get(key, f"Translation for '{key}' not found!")


get_translation()
# Rest of the code remains unchanged...

# Function for Rock, Paper, Scissors game
def get_computers_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def determine_winner(players_choice, computers_choice):
    if players_choice == computers_choice:
            return "It's a tie!"

    if (players_choice == 'p' and computers_choice == 'r') or \
            (players_choice == 'r' and computers_choice == 's') or \
            (players_choice == 's' and computers_choice == 'p'):
        return "You won!"

    return "You lost!"
determine_winner()

def play_game(language):
    print(get_translation(language, 'rps'))

    players_choice = input().lower()

    if players_choice not in ['r', 's', 'p']:
        print("Invalid choice")
        return

    computers_choice = get_computers_choice()

    print(f"\nYou chose: {players_choice}")
    print(f"The computer chose: {computers_choice}")

    result = determine_winner(players_choice, computers_choice)
    print(result)

play_game()

def calc(language):
    print(get_translation(language, 'calculator'))
    while True:
        try:
            num1 = float(input(get_translation(language, 'first_number')))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            num2 = float(input(get_translation(language, 'second_number')))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        sign = input(get_translation(language, 'operator'))
        if sign in ['+', '-', '/', '*']:
            break
        else:
            print(get_translation(language, 'invalid_operator'))

    if sign == '+':
        print(f"The result is: {num1 + num2}")
    elif sign == '-':
        print(f"The result is: {num1 - num2}")
    elif sign == '/':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Division by zero is not allowed.")
    elif sign == '*':
        print(f"The result is: {num1 * num2}")

calc()

def quiz(language):
    print(get_translation(language, 'quiz'))
    correct_answers = 0

    print("Which one was found first? (give your answer in numbers)")
    print("1) Orange the fruit")
    print("2) Orange the color")
    fq1 = input("Type: ")

    if fq1 == '1':
        print("You're right!")
        correct_answers += 1
    else:
        print("You're wrong! It was 1")

    print("Who is the best teacher in uwis?")
    print("1) Ms Urmatai")
    print("2) Mr Alladin")
    print("3) Ms Shahiya")
    print("4) All")
    fq2 = input("Type: ")

    if fq2 == '4':
        print("You're right!")
        correct_answers += 1
    else:
        print("You're wrong, it was 4")

    print("What is the capital city of France?")
    print("1) Paris")
    print("2) Madrid")
    print("3) Moscow")
    fq3 = input("Type: ")

    if fq3 == '1':
        print("You're right!")
        correct_answers += 1
    else:
        print("You're wrong, it's 1")

    print("Where is davud from?")
    print("1) kyrgyzstan")
    print("2) thailand")
    print("3) Both")
    fq4 = input("Type: ")

    if fq4 == '3':
        print("You're correct!")
        correct_answers += 1
    else:
        print("No, you're wrong")

    print("\nQuiz Complete!")
    print(f"You got {correct_answers} out of 4 questions correct.")

quiz()

def main():
    print_banner()
    language = select_language()
    print(get_translation(language, 'welcome'))

    name = input(get_translation(language, 'name_prompt'))
    print(f"Hello {name}, {get_translation(language, 'how_can_help')}")
    print("you can use the help command to see the list of functions") 

    # Define the action keywords based on the selected language
    keywords = {
        'english': {
            'calculator': ['calculator'],
            'rps': ['rps', 'play rps'],
            'quiz': ['quiz']
        },
        'russian': {
            'calculator': ['калькулятор'],
            'rps': ['камень ножницы бумага'],
            'quiz': ['викторина']
        },
        'arabic': {
            'calculator': ['آلة حاسبة'],
            'rps': ['حجر ورقة مقص'],
            'quiz': ['اختبار']
        }
    }

    while True:
        action = input(get_translation(language, 'how_can_help')).lower()



# Check if the input matches any of the action keywords in the selected language
        if any(keyword in action for keyword in keywords[language]['help']):  # Исправлено: убраны ошибки 'key worn' и пробел
            print(get_translation(language, 'available_commands'), "calculator, rps (rock-paper-scissors), quiz")  # Исправлено: добавлено сообщение с переводом
        elif any(keyword in action for keyword in keywords[language]['calculator']):  # Исправлено: заменено if на elif
            calc(language)
        elif any(keyword in action for keyword in keywords[language]['rps']):  # Исправлено: правильное название 'rock-paper-scissors'
            play_game(language)
        elif any(keyword in action for keyword in keywords[language]['quiz']):
            quiz(language)
        elif 'exit' in action:
            print(get_translation(language, 'exit'))
            break
        else:
            print(get_translation(language, 'try_again'))  # Исправлено: добавлено использование перевода


# Run the main function to start the program
main()