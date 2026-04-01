import json
import os

from config import ROOT_DIR
from src.external_api import conversion


def read_json():
    """Функция преобразования JSON файла в python"""
    try:
        way_file = os.path.join(ROOT_DIR, "data", "operations.json")
        with open(way_file, encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError as e:
        print(f"{e}")
        return []


transaction = read_json()


def transaction_withdrawal(id_transaction: int) -> float:
    """Функция вывода сумму покупки по транзакции в рублях
    если валюта не рубли идет конвертация через API запрос https://app.exchangerate-api.com/dashboard/confirmed"""

    for i in transaction:
        try:
            if i["id"] == id_transaction and i["operationAmount"]["currency"]["code"] == "RUB":
                return i["operationAmount"]["amount"]
            elif i["id"] == id_transaction and i["operationAmount"]["currency"]["code"] != "RUB":
                code = i["operationAmount"]["currency"]["code"]
                amount = i["operationAmount"]["amount"]
                total = conversion(code, amount)
                return round(total["conversion_result"], 2)
        except KeyError:
            return "id не найден"
