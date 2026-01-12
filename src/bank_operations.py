import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей и строку поиска, а возвращает словари, у которых в описании есть данная строка"""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get('description', ''))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными об операциях и список категорий операций,
    а возвращает словарь с названиями категорий и количеством операций в каждой из них"""
    result = {category: 0 for category in categories}
    for item in data:
        description = item.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1
    return result
