import json
import logging

from src.external_api import conversion

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/utils.log",
    filemode="w",
    encoding="utf-8",
)

logger = logging.getLogger("utils")


def read_json(way_file: str):
    """Функция преобразования JSON файла в python"""
    try:
        logger.info("Файл успешно преобразован")
        with open(way_file, encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError as e:
        logger.error(f"Error: {e}")
        print(f"{e}")
        return []


def transaction_withdrawal(transaction):
    """Функция вывода сумму покупки по транзакции в рублях
    если валюта не рубли идет конвертация через API запрос https://app.exchangerate-api.com/dashboard/confirmed"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Покупка в RUB; выводим сумму в RUB ")
        return transaction["operationAmount"]["amount"]
    else:
        logger.info("Покупка в иностранной валюте, конвертируем в RUB")
        code = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        total = conversion(code, amount)
        return round(total["conversion_result"], 2)
