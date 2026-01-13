import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей и строку поиска, а возвращает словари, у которых в описании есть данная строка"""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get('description', ''))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными об операциях и список категорий операций,
    а возвращает словарь с названиями категорий и количеством операций в каждой из них"""
    descriptions = []
    for item in data:
        if item.get('description', '') in categories:
            descriptions.append(item.get('description', ''))
    counted = Counter(descriptions)
    return counted
