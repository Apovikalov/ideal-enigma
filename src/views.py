import datetime as dt
import json
import logging
import os
# import urllib.request
from datetime import datetime
from typing import Any, Dict, List

# import requests
from dotenv import load_dotenv

# from src.utils import read_json, read_xlsx, write_json

load_dotenv()  # Получение API ключа из моего окружения
API_KEY_CUR = os.getenv("API_KEY_CUR")

SP_500_API_KEY = os.getenv("SP_500_API_KEY")

logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler("utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

with open(r"C:\PythonProject1\settings.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def greeting_time(date_and_time: Any):
    """Принимает строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает приветствие с соответствующим временем суток."""
    if date_and_time is None:
        date_and_time = datetime.now()
    elif type(date_and_time) is str:
        date_and_time = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
    hours = date_and_time.hour
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


def for_each_card(my_list: list) -> list:
    """Функция обрабатывает данные о картах из списка"""
    logger.info("Начало работы функции (for_each_card)")
    cards = {}
    result = []
    logger.info("Перебор транзакций")
    for i in my_list:
        if i["Номер карты"] == "nan" or type(i["Номер карты"]) is float:
            continue
        elif i["Сумма платежа"] == "nan":
            continue
        else:
            if i["Номер карты"][1:] in cards:
                cards[i["Номер карты"][1:]] += float(str(i["Сумма платежа"])[1:])
            else:
                cards[i["Номер карты"][1:]] = float(str(i["Сумма платежа"])[1:])
    for k, v in cards.items():
        result.append({"last_digits": k, "total_spent": round(v, 2), "cashback": round(v / 100, 2)})
    logger.info("Завершение работы функции (for_each_card)")
    return result


def top_5_transactions(my_list: list) -> list:
    """Функция возвращает топ 5 транзакций"""
    logger.info("Начало работы функции (top_five_transaction)")
    all_transactions = {}
    result = []
    logger.info("Перебор транзакций в функции (top_five_transaction)")
    for i in my_list:
        if i["Категория"] not in all_transactions and str(i["Сумма платежа"])[0:1] != "-":
            if i["Категория"] != "Пополнения":
                all_transactions[i["Категория"]] = float(str(i["Сумма платежа"])[1:])
        elif (
                i["Категория"] in all_transactions
                and float(str(i["Сумма платежа"])[1:]) > all_transactions[i["Категория"]]
        ):
            all_transactions[i["Категория"]] = float(str(i["Сумма платежа"])[1:])
    for i in my_list:
        for k, v in all_transactions.items():
            if k == i["Категория"] and v == float(str(i["Сумма платежа"])[1:]):
                result.append({"date": i["Дата платежа"].strftime('%d.%m.%Y'),
                               "amount": v, "category": k, "description": i["Описание"]})
    logger.info("Окончание работы функции (top_five_transaction)")

    return result


def currency_rates(currency: list) -> list[dict]:
    """Функция запроса курса валют"""
    logger.info("Начало работы функции (currency_rates)")
    result = []
    for i in currency:
        for j in range(len(data["currency_rates"])):
            if data["currency_rates"][j]["currency"] == i:
                result.append({"currency": i, "rate": data["currency_rates"][j]["rate"]})

    logger.info("Создание списка словарей для функции - currency_rates")

    logger.info("Окончание работы функции - currency_rates")
    return result


def get_price_stock(stocks: list) -> list:
    """Функция для получения данных об акциях из списка S&P500"""
    logger.info("Начало работы функции (get_price_stock)")
    stock_prices = []
    logger.info("Функция обрабатывает данные транзакций.")
    for stock in stocks:
        for j in range(len(data["stock_prices"])):
            if data["stock_prices"][j]["stock"] == stock:
                stock_prices.append({"stock": stock, "price": data["stock_prices"][j]["price"]})
    logger.info("Функция get_price_stock успешно завершила свою работу")
    return stock_prices


def filter_by_date(date: str, my_list: list) -> list:
    """Функция фильтрующая данные по заданной дате"""
    list_by_date = []
    logger.info("Начало работы функции (filter_by_date)")
    if date == "":
        return list_by_date
    year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
    date_obj = dt.datetime(year, month, day)
    for i in my_list:
        if type(i) is dict:
            if i["Дата платежа"] == "nan" or type(i["Дата платежа"]) is float:
                continue
            elif (
                    date_obj
                    >= dt.datetime.strptime(str(i["Дата платежа"]), "%d.%m.%Y")
                    >= date_obj - dt.timedelta(days=day - 1)
            ):
                list_by_date.append(i)
    logger.info("Конец работы функции (filter_by_date)")
    return list_by_date
