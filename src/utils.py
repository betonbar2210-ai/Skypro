import json
from src.external_api import conversion


def read_json(way_file: str):
    """Функция преобразования JSON файла в python"""
    try:
        with open(way_file, encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError as e:
        print(f"{e}")
        return []





def transaction_withdrawal(transaction):
    """Функция вывода сумму покупки по транзакции в рублях
    если валюта не рубли идет конвертация через API запрос https://app.exchangerate-api.com/dashboard/confirmed"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        code = transaction.get("operationAmount", {}).get("currency",{}).get("code")
        amount = transaction.get("operationAmount", {}).get("amount")
        total = conversion(code, amount)
        return round(total["conversion_result"], 2)

