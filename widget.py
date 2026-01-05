from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счёта"""
    split_list = card_number.split(' ')
    if split_list[0] == 'Счет':
        masked = get_mask_account(str(split_list[-1]))
    else:
        masked = get_mask_card_number(str(split_list[-1]))
    split_list[-1] = masked
    complete_number = ' '.join(split_list)
    return complete_number


def get_date(date_and_time: str) -> str:
    """Возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    complete_date = date_and_time[8:10]
    complete_date += '.'
    complete_date += date_and_time[5:7]
    complete_date += '.'
    complete_date += date_and_time[0:4]
    return complete_date
