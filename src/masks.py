import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

logger = logging.getLogger("masks")


def get_mask_card_number(number_card: str) -> str:
    """Функция скрытие номера карты"""
    if len(number_card) < 16:
        logger.warning(f"Некорректный номер карты: {number_card}. Ожидалось 16 цифр")
        return "Введен некоректный номер карты\n"
    else:
        logger.info("Выводим замаскированный номер карты")
        card_mask = f"{number_card[0:-12]} {number_card[-12:-10]}** **** {number_card[-4:]}\n"
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция скрытия номера счета"""
    if "Счет" in account_number and len(account_number) > 20:
        logger.info("Замаскирован номер счета")
        return f"Счет **{account_number[-4:]}\n"
        logger.warning(f"Некорректный номер счёта: {account_number}")
        return "Введен некоректный номер счета\n"
    else:
        logger.warning(f"Некорректный номер счёта: {account_number}")
        return "Введен некоректный номер счета\n"
