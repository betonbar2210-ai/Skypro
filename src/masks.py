from typing import Optional


def get_mask_card_number(number_card: str) -> Optional[str]:
    """Функция скрытие номера карты"""
    card_mask = f"{number_card[0:-12]} {number_card[-12:-10]}** **** {number_card[-4:]}\n"
    return card_mask


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция скрытия номера счета"""
    return f"{account_number[0:-20]}**{account_number[-4:]}\n"
