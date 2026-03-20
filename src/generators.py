from typing import Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Функция возврата итератора,
    который поочередно выдает транзакции, по ключу code(например, USD)"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list, request: str) -> Iterator[str]:
    """генератор, принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if request in transaction:
            yield transaction[request]


def card_number_generator(start: int, finish: int) -> Generator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    while start <= finish:
        format_card = format(start, "016")
        yield f"{format_card[:4]} {format_card[4:8]} {format_card[8:12]} {format_card[12:]}"
        start += 1
