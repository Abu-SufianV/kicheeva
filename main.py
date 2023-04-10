from db_integration import *
import speech_recognition as sr
from time import sleep
import pandas as pd


def formatted_print_data(product_data: list[tuple]) -> None:
    """
    Форматированный вывод таблицы

    :param product_data: Список товаров
    """
    df = pd.DataFrame(data=product_data, columns=['ID', 'Название', 'Тип товара', 'Цена', 'Кол-во'])
    res = df.to_string(index=False)
    print(res)


def voice_to_text() -> str:
    """
    Функция преобразует запись с микрофона в текст
    :return: Расшифрованный текст
    """
    record = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print('\nСлушаю...\n')
        audio = record.listen(source)

    query = record.recognize_google(audio, language='ru-RU')
    print(f'Ваш запрос: {query}')
    return query


def find_product(query: str):
    split_query = query.lower().split()

    signs = {
        'больше': '>',
        'меньше': '<',
        'равна':  '=',
        'равным': '=',
        'равное': '=',
    }
    if 'названию' in split_query:
        data = find_product_by_name(split_query[-1].capitalize())
        formatted_print_data(data)
    elif 'всех' in split_query:
        data = list_all_products()
        formatted_print_data(data)
    elif 'типу' in split_query:
        data = find_product_by_type(split_query[-1].capitalize())
        formatted_print_data(data)
    elif 'цена' or 'ценой' in split_query:
        sign = signs[split_query[-2]]
        price = split_query[-1].replace('.', '')

        data = find_product_by_price(price, sign)
        formatted_print_data(data)

if __name__ == '__main__':
    print('Добрый день! Я голосовой помощник, помогу Вам найти товар в БД :)')
    while True:
        try:
            text = voice_to_text()
        except Exception:
            print('Я ничего не слышу ;(\n'
                  'Проверьте микрофон'
                  '\n\nP. S. Если  Вы закончили искать товары, то просто скажите "Стоп" и программа отключится')
            continue


        try:
            if text == 'стоп':
                print('\nРабота программы завершена!')
                break
            find_product(text)
            sleep(3)
            print()
        except Exception as error:
            print(f"Ошибка записи: {error}")
