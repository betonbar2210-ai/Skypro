import re
from collections import Counter

from tests.conftest import utils_json, test_csv


def process_bank_search(test_csv, search):
    """Функция фильтрации списка словорей по строке поиска"""
    pattern = re.compile(search, re.IGNORECASE)
    filtered_data = []
    for operation in test_csv:
        if "description" in operation and pattern.search(operation["description"]):
            filtered_data.append(operation)
    return filtered_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция сортировки списка словарей и вывод
    Словаря в формате Категория: количество операций"""
    category_count = []
    for operation in data:
        for cat in categories:
            if cat in operation.get("description"):
                category_count.append(operation["description"])
                break
    count_dict = Counter(category_count)
    return count_dict



