from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_user: str) -> str:
    """Функция обработки введенных данных Счет или Карта
    и вывода замаскированной информации"""
    user_card = get_mask_card_number(info_user)
    user_number = get_mask_account(info_user)
    if "Счет" in info_user:
        return user_number
    else:
        return user_card


def get_date(line_date: str) -> str:
    """Функция возврата времени в формате ДД.ММ.ГГГГ"""
    if not line_date.strip():
        return "Дата отсутствует"
    try:
        data_in = datetime.fromisoformat(line_date)
        return data_in.strftime("%d.%m.%Y")
    except ValueError:
        return "Недопустимый формат даты"
