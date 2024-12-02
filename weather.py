import requests

def get_weather(city):
    api_key = "0c76d83cd67b55deff4e1332b3ede127"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Погода в {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print("Ответ сервера:", response.text)  # Полный ответ сервера для отладки
        print("Не удалось получить данные. Проверьте название города.")

city = input("Введите название города: ")
get_weather(city)
