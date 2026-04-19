from src.output_of_categories import process_bank_operations, process_bank_search
from tests.conftest import test_csv


def test_process_bank_search(test_csv):
    assert process_bank_search(test_csv, "Перевод") == test_csv
    assert process_bank_search(test_csv, "перевод") == test_csv
    assert process_bank_search(test_csv, "Любое слово") == []


def test_process_bank_operations(test_csv):
    assert process_bank_operations(test_csv, ["Перевод организации"]) == {"Перевод организации": 1}
    assert process_bank_operations(test_csv, ["Перевод организации", "Перевод с"]) == {
        "Перевод организации": 1,
        "Перевод с карты на карту": 1,
    }
