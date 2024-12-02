def translator(language, phrase):
    translations = {
        'en': {
            'hello': 'Hello',
            'bye': 'Goodbye',
            'thank_you': 'Thank you'
        },
        'ru': {
            'hello': 'Привет',
            'bye': 'До свидания',
            'thank_you': 'Спасибо'
        }
    }

    return translations.get(language, {}).get(phrase, "Translation not available")

# Пример использования
language = input("Choose a language (en/ru): ").strip().lower()
phrase = input("Enter a phrase to translate (hello/bye/thank_you): ").strip().lower()

translation = translator(language, phrase)
print(f"Translation: {translation}")
