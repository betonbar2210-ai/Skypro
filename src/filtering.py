from src.output_of_categories import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_xlsl import reader_csv, reader_excel
from src.utils import read_json


def read_file():
    """Чтение файлов на выбор JSON, CSV, EXCEL"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    user_answer_1 = input(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )
    while True:
        if user_answer_1 == "1":
            print("Для обработки выбран JSON-файл\n")
            json_file = read_json("data/operations.json")
            return json_file
        elif user_answer_1 == "2":
            print("Для обработки выбран CSV-файл\n")
            csv_file = reader_csv("data/transactions.csv")
            return csv_file
        elif user_answer_1 == "3":
            print("Для обработки выбран XLSX-файл\n")
            excel_file = reader_excel("data/transactions_excel.xlsx")
            return excel_file
        else:
            user_answer_1 = input(
                "Введен некорректный номер\n"
                "Выберите необходимый пункт меню:\n"
                "1 Получить информацию о транзакциях из JSON-файла\n"
                "2 Получить информацию о транзакциях из CSV-файла\n"
                "3 Получить информацию о транзакциях из XLSX-файла\n"
            )


def filter_status():
    """Фильтрация по статусам"""
    filter_file = read_file()
    user_answer_2 = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    ).upper()
    while True:
        if user_answer_2 == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            executed_file = filter_by_state(filter_file, user_answer_2)
            return executed_file

        elif user_answer_2 == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            cancel_file = filter_by_state(filter_file, user_answer_2)
            return cancel_file

        elif user_answer_2 == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            pen_file = filter_by_state(filter_file, user_answer_2)
            return pen_file

        else:
            user_answer_2 = input(
                f'Статус операции "{user_answer_2}" недоступен'
                f"Введите статус, по которому необходимо выполнить фильтрацию."
                f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            ).upper()


def sort_date():
    """Сортировка по датам (убывание/возрастание)"""
    sort_file = filter_status()
    user_answer_3 = input("Отсортировать операции по дате?\nДа/Нет\n").lower()
    if "да" in user_answer_3:
        user_answer_4 = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        while True:
            if "по убыванию" in user_answer_4:
                descending_list = sort_by_date(sort_file)
                return descending_list
            elif "по возрастанию" in user_answer_4:
                increasing_list = sort_by_date(sort_file, type_filter=False)
                return increasing_list
            else:
                user_answer_4 = input(
                    f"Команда {user_answer_4} не распознана, введите:\n" f"по убыванию\n" f"по возрастанию\n"
                )
    else:
        return sort_file


def sort_rub():
    """Сортируем по валютам если надо"""
    result_file = sort_date()
    user_answer_5 = input("Выводить только рублевые транзакции?\nДа/Нет\n").lower()
    if "да" in user_answer_5:
        sort_r = []
        for transaction in result_file:
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
                sort_r.append(transaction)
            elif transaction.get("currency_code") == "RUB":
                sort_r.append(transaction)
        return sort_r
    else:
        return result_file


def filter_word():
    """Фильтрация по ключевым запросам"""
    finish_file = sort_rub()
    user_answer_5 = input("Отфильтровать список транзакций по определенному слову в описании?\nДа/Нет\n").lower()
    if "да" in user_answer_5:
        user_answer_6 = input("По какому слову фильтровать:\n").lower()
        file_sort = process_bank_search(finish_file, user_answer_6)
        return file_sort
    else:
        return finish_file
