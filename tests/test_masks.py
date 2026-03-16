from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_type, expected",
    [
        ("Master 1111112345678956", "Master 1111 11** **** 8956\n"),
        ("Visa 1111112345678956", "Visa 1111 11** **** 8956\n"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361\n"),
    ],
)
def test_mask_card(card_type, expected):
    assert get_mask_card_number(card_type) == expected


def test_mask_card_number():
    assert get_mask_card_number("123456789112345") == "Введен некоректный номер карты\n"
    assert get_mask_card_number("") == "Введен некоректный номер карты\n"


def test_get_mask_account():
    assert get_mask_account("Счет 12345678911234567892") == "Счет **7892\n"
    assert get_mask_account("") == "Введен некоректный номер счета\n"
    assert get_mask_account("Счет 00") == "Введен некоректный номер счета\n"
    assert get_mask_account("12345678911234567892") == "Введен некоректный номер счета\n"
