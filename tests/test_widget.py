from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Счет 12345678911234567892") == "Счет **7892\n"
    assert mask_account_card("") == "Введен некоректный номер карты\n"
    assert mask_account_card("Счет 123") == "Введен некоректный номер счета\n"
    assert mask_account_card("Master 1111112345678956") == "Master 1111 11** **** 8956\n"
    assert mask_account_card("123456789112345") == "Введен некоректный номер карты\n"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == "Дата отсутствует"
    assert get_date("invalid-date-format") == "Недопустимый формат даты"
