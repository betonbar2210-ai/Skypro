def get_mask_card_number(number_card: str) -> str:
    """Функция скрытие номера карты"""
    if len(number_card) < 16:
        return "Введен некоректный номер карты\n"
    else:
        card_mask = f"{number_card[0:-12]} {number_card[-12:-10]}** **** {number_card[-4:]}\n"
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция скрытия номера счета"""
    if len(account_number) < 20 or "Счет" not in account_number:
        return "Введен некоректный номер счета\n"
    else:
        return f"{account_number[0:-20]}**{account_number[-4:]}\n"
