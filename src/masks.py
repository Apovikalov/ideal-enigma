import logging

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

masks_file_handler = logging.FileHandler("logs/masks.log", mode="w")
masks_file_handler.setLevel(logging.DEBUG)

masks_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)

masks_logger.addHandler(masks_file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    masked = str(card_number)[0:4]
    masked += " "
    masked += str(card_number)[4:6]
    masked += "** **** "
    masked += str(card_number)[-4:]
    masks_logger.info(f"Получена маска номера карты: {masked}")
    return masked


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    masked = "**"
    masked += str(account_number)[-4:]
    masks_logger.info(f"Получена маска номера счёта: {masked}")
    return masked
