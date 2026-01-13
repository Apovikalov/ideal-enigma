import json
import logging
import os

# import re
# from datetime import datetime
from masks import get_mask_account, get_mask_card_number
# from src.utils import load_transactions
from src.config import DATA_DIR, LOG_DIR
from src.data_reader import filter_transactions, read_transactions_from_csv, read_transactions_from_excel
from widget import get_date

# import pandas as pd


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(), logging.FileHandler(os.path.join(LOG_DIR, "app.log"), encoding="utf-8")],
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# Функция загрузки транзакций из файла
def load_transactions(file_path: str):
    if file_path.endswith(".json"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                transactions = json.load(file)
                return transactions
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
            raise
    elif file_path.endswith(".csv"):
        transactions = read_transactions_from_csv(file_path)
        return transactions
    elif file_path.endswith(".xlsx"):
        transactions = read_transactions_from_excel(file_path)
        return transactions
    else:
        logger.error(f"Неподдерживаемый формат файла: {file_path}")
        raise ValueError("Unsupported file format")


# Функция для формата вывода информации о транзакциях
def format_transaction(transaction):
    # Получаем дату и описание
    date = transaction.get("date", "Не указано")
    description = transaction.get("description", "Не указано")

    # Получаем сумму и валюту
    amount = transaction.get("operationAmount", {}).get("amount", "Не указано")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "Не указано")

    # Получаем информацию о счете откуда и куда
    from_account = transaction.get("from", "Не указано")
    to_account = transaction.get("to", "Не указано")

    # Форматируем вывод
    output = f"{date} {description}\n"
    output += f"{from_account} -> {to_account}\n"
    output += f"Сумма: {amount} {currency}\n"
    return output


def print_transaction(transaction):
    """Выводит информацию о транзакции в требуемом формате."""
    date = get_date(transaction["date"])
    description = transaction["description"]

    # Получаем значения from и to, обрабатываем пустые значения
    from_account = transaction.get("from", "")
    to_account = transaction.get("to", "")

    # Заменяем NaN или пустую строку на пробел
    if isinstance(from_account, float) or not from_account:
        from_account = " "  # Заменить NaN или пустую строку на пробел
    if isinstance(to_account, float) or not to_account:
        to_account = " "  # Заменить NaN или пустую строку на пробел

    # Маскировка
    if "карта" in description.lower():  # Если это перевод с карты на карту
        from_account = get_mask_card_number(from_account) if from_account != " " else from_account
        to_account = get_mask_card_number(to_account) if to_account != " " else to_account
    else:
        from_account = get_mask_account(from_account) if "счет" in str(from_account).lower() \
            else get_mask_card_number(from_account)
        to_account = get_mask_account(to_account) if "счет" in str(to_account).lower() \
            else get_mask_card_number(to_account)

    # Форматируем вывод в зависимости от типа операции
    if "перевод" in description.lower():
        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
    elif "открытие вклада" in description.lower():
        print(f"{date} {description}")
        print(f"{to_account}")  # Выводим только to_account
    else:
        print(f"{date} {description}")
        print(f"{from_account}")

    # Проверка на наличие ключа 'operationAmount'
    if "operationAmount" in transaction:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]
        print(f"Сумма: {amount} {currency}\n")
    else:
        print("Сумма: \n")  # информация отсутствует


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        file_path = os.path.join(DATA_DIR, "operations.json")
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = os.path.join(DATA_DIR, "transactions.csv")
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. "
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
            )
            .strip()
            .upper()
        )
        if status in statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status}"')
            filtered_transactions = [
                t for t in transactions if str(t.get("state", "")).upper() == status
            ]  # Преобразование в строку
            break
        else:
            print(f'Программа: Статус операции "{status}" недоступен.')

    # Дополнительные фильтры
    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Сортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        if order_choice == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif order_choice == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [
            t
            for t in filtered_transactions
            if "operationAmount" in t and t["operationAmount"]["currency"]["code"] == "RUB"
        ]

    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if description_filter == "да":
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions(filtered_transactions, search_string)

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
