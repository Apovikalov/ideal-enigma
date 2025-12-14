def filter_by_currency(transactions: list, currency_name: str):
    """возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    complete_transactions = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency_name:
            complete_transactions.append(transaction)
    for i in complete_transactions:
        yield i


def transaction_descriptions(transactions: list):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    desc_list = []
    for transaction in transactions:
        desc_list.append(transaction["description"])
    for i in desc_list:
        yield i


def card_number_generator(start: int, end: int):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        # Форматируем номер с ведущими нулями, если это необходимо
        card_number = f"{number:016d}"
        # Форматируем номер с пробелами
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
