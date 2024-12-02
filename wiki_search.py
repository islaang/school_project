import requests
import urllib.parse

def wiki_search(query):
    # Кодируем запрос в формат URL
    query = urllib.parse.quote(query)
    url = f"https://ru.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={query}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        search_results = data.get('query', {}).get('search', [])
        
        if search_results:
            print("Результаты поиска:")
            for i, result in enumerate(search_results[:3], start=1):  # Ограничиваем вывод 3 результатами
                print(f"{i}. {result['title']} - https://ru.wikipedia.org/wiki/{result['title']}")
        else:
            print("Нет результатов для вашего запроса.")
    else:
        print("Ошибка при запросе к Википедии.")

# Ввод запроса
query = input("Введите запрос для поиска в Википедии: ")
wiki_search(query)
