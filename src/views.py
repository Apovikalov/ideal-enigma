import json
import os
from typing import Any, Dict, List
from datetime import datetime

import requests
import yfinance as yf
from dotenv import load_dotenv

from src.utils import read_json, read_xlsx, write_json

load_dotenv()
# Получение API ключа из моего окружения
API_KEY = os.getenv("api_key")

def greeting_time(date_and_time: Any):
    """Принимает строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает приветствие с соответствующим временем суток."""
    if date_and_time is None:
        date_and_time = datetime.now()
        hours = date_and_time.hour
    else:
        hours = int(date_and_time[11:13])
    greet = ""
    if 0 <= hours <= 5:
        greet = "Доброй ночи!"
    elif 6 <= hours <= 11:
        greet = "Доброе утро!"
    elif 12 <= hours <= 17:
        greet = "Добрый день!"
    elif 18 <= hours <= 23:
        greet = "Добрый вечер!"
    return greet


def calculate_total_expenses(transactions_sum: List[Dict[str, Any]]) -> float:
    """Функция считает сумму расходов по списку транзакций."""
    total_expenses = 0.0
    for transaction in transactions_sum:
        if transaction["Сумма платежа"] < 0:
            total_expenses += transaction["Сумма платежа"]
    return total_expenses * -1


def proc_card_data(operat: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция обрабатывает данные о картах из списка."""
    card_data = {}
    for operation in operat:
        if isinstance(operation["Номер карты"], str) and operation["Номер карты"].startswith("*"):
            last_digits = operation["Номер карты"][-4:]
            if last_digits not in card_data:
                card_data[last_digits] = {"last_digits": last_digits, "Сумма операции": 0.0, "Кэшбэк": 0.0}
            if operation["Сумма платежа"] < 0:
                card_data[last_digits]["Сумма операции"] += round(operation["Сумма платежа"] * -1, 1)
            # card_data[last_digits]["Кэшбэк"] += operation.get("Бонусы (включая кэшбэк)", 0.0)
    return list(card_data.values())


def top_5_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция возвращает топ 5 транзакций"""
    transactions.sort(key=lambda x: x["Сумма платежа"], reverse=True)
    return transactions[:5]


# def get_cur_rate(currency: str) -> Any:
#    """Функция получает курс валют"""
#    url = f"https://www.x-rates.com/table/?from=USD&amount=1"
#    response = requests.get(url, headers={"apikey": API_KEY}, timeout=40)
#    response_data = json.loads(response.text)
#    return response_data["rates"]["RUB"]


def get_stock_cur(stock: str) -> Any:
    """Функция получает акции с помощью Yahoo Finance"""
    stock_data = yf.Ticker(stock)
    todays_data = stock_data.history(period="1d")
    return todays_data["High"].iloc[0]


def main_views() -> None:
    """
    Главная функция программы, запускающая все функции модулей.
    """
    user_input = input(
        "Введите date и time в формате YYYY-MM-DD HH:MM:SS " "или нажмите Enter для использования на вашем устройстве:"
    )
    greeting = greeting_time(user_input if user_input else None)
    transactions = read_xlsx("../data/operations.xlsx")
    total_expenses = calculate_total_expenses(transactions)
    card_data = proc_card_data(transactions)
    top_trans = top_5_transactions(transactions)
#    currency_rates = [
#        {"currency": "USD", "rate": get_cur_rate("USD")},
#        {"currency": "EUR", "rate": get_cur_rate("EUR")},
#    ]
    stock_prices = [
        {"stock": "AAPL", "price": get_stock_cur("AAPL")},
        {"stock": "AMZN", "price": get_stock_cur("AMZN")},
        {"stock": "GOOGL", "price": get_stock_cur("GOOGL")},
        {"stock": "MSFT", "price": get_stock_cur("MSFT")},
        {"stock": "TSLA", "price": get_stock_cur("TSLA")},
    ]
    output_data = {
        "greeting": greeting,
        "total_expenses": total_expenses,
        "card_data": card_data,
        "top_transactions": top_trans,
#        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
    output_file = "operations_data.json"
    write_json(output_file, output_data)
    print(read_json(output_file))


if __name__ == "__main__":
    main_views()
