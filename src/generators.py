from typing import Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Функция возврата итератора,
    который поочередно выдает транзакции, по ключу code(например, USD)"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction

def transaction_descriptions(transactions: list) -> Iterator[str]:
    """генератор, принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction["description"]
