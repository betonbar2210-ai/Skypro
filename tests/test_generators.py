from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions):
    result = filter_by_currency(test_transactions, "RUB")
    assert next(result, "валюта не найдена") == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    result_non = filter_by_currency(test_transactions, "")
    assert next(result_non, "валюта не найдена") == "валюта не найдена"


def test_transaction_descriptions(test_transactions):
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"