import json
from pathlib import Path

from src.reports import spending_by_category
from src.services import simple_search
from src.utils import read_xlsx
from src.views import (calculate_total_expenses, currency_rates, filter_by_date, for_each_card, get_price_stock,
                       greeting_time, top_5_transactions)

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
my_list = read_xlsx(file_path)

with open(r"C:\PythonProject1\settings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

currencies = []
for i in range(len(data["currency_rates"])):
    currencies.append(data["currency_rates"][i]["currency"])

stocks = []
for i in range(len(data["stock_prices"])):
    stocks.append(data["stock_prices"][i]["stock"])


def run_all_functions():
    """Запускает все функции из модулей views, reports, services"""
    print("Запуск страницы Главная")
    greeting = greeting_time(None)
    expenses = calculate_total_expenses(my_list)
    each_card = for_each_card(my_list)
    top_5 = top_5_transactions(my_list)
    rates = currency_rates(currencies)
    stock_price = get_price_stock(stocks)
    fbd = filter_by_date("", "../data/operations.xlsx")
    for j in [greeting, expenses, each_card, top_5, rates, stock_price, fbd]:
        print(j)
    print("Запуск страницы Сервисы")
    search = simple_search(my_list, "Ozon.ru")
    print(search)
    print("Запуск страницы Отчеты")
    spend = spending_by_category(my_list, "Переводы", date="31.12.2021")
    print(spend)


run_all_functions()
