import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем статус ответа ВСТАВКА

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

    # НАЧАЛО ВСТАВКИ

        # Инициализируем переводчик
        translator = Translator()

        # Переводим слово и его определение на русский язык
        translated_word = translator.translate(english_words, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

    # КОНЕЦ ВСТАВКИ

        # Чтобы программа возвращала словарь
        return {
            "english_words": translated_word,
            "word_definition": translated_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")

        # Возвращаем пустой словарь в случае ошибки ВСТАВКА
        return {
            "english_words": "",
            "word_definition": ""
        }

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Проверяем, что слово и определение не пустые ВСТАВКА
        if not word or not word_definition:
            print("Не удалось получить слово и его определение. Попробуйте снова.")
            continue

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()
