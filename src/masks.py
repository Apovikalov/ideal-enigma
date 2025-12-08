def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    if len(card_number) == 16:
        masked = card_number[0:4]
        masked += " "
        masked += card_number[4:6]
        masked += "** **** "
        masked += card_number[-4:]
    elif len(card_number) == 13:
        masked = card_number[0:6]
        masked += "***"
        masked += card_number[-4:-1]
        masked += " "
        masked += card_number[-1]
    return masked
