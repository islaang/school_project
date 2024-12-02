import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = "bca99fb36183b1ca3275f48c5f00fa60"  # Ваш API ключ
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'result' in data:
            print(f"{amount} {from_currency} = {data['result']} {to_currency}")
        else:
            print("Ошибка: API не вернул ожидаемое поле 'result'. Проверьте параметры запроса.")
    else:
        print("Не удалось выполнить запрос к API.")

# Пример использования
amount = float(input("Введите сумму: "))
from_currency = input("Из какой валюты (например, USD): ").upper()
to_currency = input("В какую валюту (например, KGS): ").upper()
currency_converter(amount, from_currency, to_currency)
