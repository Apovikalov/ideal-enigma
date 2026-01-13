def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    masked = ""
    if card_number.isdigit():
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
    else:
        split_list = card_number.split(" ")
        complete_mask = split_list[0] + " "
        card_number = split_list[-1]
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
        complete_mask += masked
        return complete_mask


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    masked = "**"
    masked += account_number[-4:]
    return masked
