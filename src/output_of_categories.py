import re


def process_bank_search(test_csv, search):
    """Функция фильтрации списка словорей по строке поиска"""
    pattern = re.compile(search, re.IGNORECASE)
    filtered_data = []
    for operation in test_csv:
        if 'description' in operation and pattern.search(operation['description']):
            filtered_data.append(operation)
    return filtered_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция сортировки списка словорей и вывод
    Словаря в формате Категория : количество операций"""
    category_counts = {}
    for category in categories:
        category_counts[category] = 0
    for operation in data:
        description = operation.get('description')
        if not description:
            continue
        for category in categories:
            if category in description:
                category_counts[description] += 1
                break
    return category_counts


