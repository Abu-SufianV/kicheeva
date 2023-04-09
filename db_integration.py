"""
Скрипт интеграции с БД

Возможен поиск товара по раным параметрам 
"""
import sqlite3 as sql


def find_product_by_name(name: str) -> list[tuple]:
    try:
        with sql.connect('./db.sqlite') as db:
            cursor = db.cursor()

            result = cursor.execute(f'SELECT * FROM products WHERE product_name = "{name}"').fetchall()

            return result
    except Exception as error:
        print(f'ERROR: Ошибка при поиске товара по названию "{name}": {error}')


def find_product_by_type(product_type: str) -> list[tuple]:
    try:
        with sql.connect('./db.sqlite') as db:
            cursor = db.cursor()

            result = cursor.execute(f'SELECT * FROM products WHERE product_type = "{product_type}"').fetchall()

            return result
    except Exception as error:
        print(f'ERROR: Ошибка при поиске товара по типу "{product_type}": {error}')


def find_product_by_price(price: str, sign: str) -> list[tuple]:
    try:
        with sql.connect('./db.sqlite') as db:
            cursor = db.cursor()

            result = cursor.execute(f'SELECT * FROM products WHERE price {sign} {price}').fetchall()

            return result
    except Exception as error:
        print(f'ERROR: Ошибка при поиске товара по цене {sign} {price}: {error}')


def find_product_by_amount(amount: str, sign: str) -> list[tuple]:
    try:
        with sql.connect('./db.sqlite') as db:
            cursor = db.cursor()

            result = cursor.execute(f'SELECT * FROM products WHERE price {sign} {amount}').fetchall()

            return result
    except Exception as error:
        print(f'ERROR: Ошибка при поиске товара по количеству {sign} {amount}: {error}')


def list_all_products() -> list[tuple]:
    try:
        with sql.connect('./db.sqlite') as db:
            cursor = db.cursor()

            result = cursor.execute(f'SELECT * FROM products').fetchall()

            return result
    except Exception as error:
        print(f'ERROR: Ошибка при запросе всех товаров: {error}')
