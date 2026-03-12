def filter_by_state(list_dict_1: list, state: str = "EXECUTED") -> list:
    """Функция возврата списка по ключу 'state'"""
    filter_list = []
    for x in list_dict_1:
        if "state" in x and x["state"] == state:
            filter_list.append(x)
    return filter_list


def sort_by_date(list_data: list, type_filter: bool = True) -> list:
    """Функция возврата отсортированного списка по датам,
    порядок по умолчанию - по убыванию"""
    sort_list = sorted(list_data, key=lambda x: x["date"], reverse=type_filter)
    return sort_list
