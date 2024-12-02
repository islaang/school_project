questions = {
    "Столица Франции?": "Париж",
    "Сколько планет в Солнечной системе?": "8",
    "Кто написал 'Война и мир'?": "Толстой"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно! Правильный ответ: {answer}")

print(f"Вы ответили правильно на {score} из {len(questions)} вопросов.")
