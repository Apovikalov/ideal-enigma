def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    masked = str(card_number)[0:4]
    masked += " "
    masked += str(card_number)[4:6]
    masked += "** **** "
    masked += str(card_number)[-4:]
    return masked


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    masked = "**"
    masked += str(account_number)[-4:]
    return masked
