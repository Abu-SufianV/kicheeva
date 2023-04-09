from db_integration import *
from pprint import pprint
import pandas as pd


# TODO: Доделалть форматированный вывод таблицы, есть нужные библиотеки, погуглить
def formatted_print_data(product_data: list[tuple]) -> None:
    # prepared_data = [headers, *product_data]
    df = pd.DataFrame(data=product_data, columns=['ID', 'Название', 'Тип товара', 'Цена', 'Кол-во'])

    # for row in prepared_data:
    #     print(*row, sep=' \t\t')

    print(df.head(10))


def voice_to_text():
    pass


if __name__ == '__main__':
    formatted_print_data(list_all_products())
