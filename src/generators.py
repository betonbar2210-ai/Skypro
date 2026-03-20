from typing import Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Функция возврата итератора,
    который поочередно выдает транзакции, по ключу code(например, USD)"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction