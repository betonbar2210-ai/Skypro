import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='logs/masks.log',
                    filemode='w',
                    encoding='utf-8')

logger = logging.getLogger('masks')


def get_mask_card_number(number_card: str) -> str:
    """Функция скрытие номера карты"""
    if len(number_card) != 16 or not number_card.isdigit():
        logger.warning(f'Некорректный номер карты: {number_card}. Ожидалось 16 цифр')
        return f'Некорректный номер карты: {number_card}. Ожидалось 16 цифр\n'
    else:
        logger.info('Выводим замаскированный номер карты')
        card_mask = f"{number_card[0:-12]} {number_card[-12:-10]}** **** {number_card[-4:]}\n"
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция скрытия номера счета"""
    if len(account_number) < 20 or "Счет" not in account_number:
        logger.warning(f'Некорректный номер счёта: {account_number}')
        return "Введен некоректный номер счета\n"
    else:
        logger.info('Замаскирован номер счета')
        return f"{account_number[0:-20]}**{account_number[-4:]}\n"