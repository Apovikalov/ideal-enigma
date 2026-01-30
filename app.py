import json
from pathlib import Path

from src.reports import spending_by_category
from src.services import simple_search
from src.utils import read_xlsx
from src.views import (calculate_total_expenses, currency_rates, filter_by_date, for_each_card, get_price_stock,
                       greeting_time, top_5_transactions)

file_path = str(Path(__file__).resolve().parent.parent) + "PythonProject1\\data\\operations.xlsx"
my_list = read_xlsx(file_path)

with open(r"C:\PythonProject1\settings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

currencies = []
for i in range(len(data["currency_rates"])):
    currencies.append(data["currency_rates"][i]["currency"])

stocks = []
for i in range(len(data["stock_prices"])):
    stocks.append(data["stock_prices"][i]["stock"])


def app():
    print("Запуск страницы Главная")
    greeting_time(None)
    calculate_total_expenses(my_list)
    for_each_card(my_list)
    top_5_transactions(my_list)
    currency_rates(currencies)
    get_price_stock(stocks)
    filter_by_date("", "../data/operations.xlsx")
    print("Запуск страницы Сервисы")
    simple_search(my_list, "Ozon.ru")
    print("Запуск страницы Отчеты")
    spending_by_category(my_list, "Переводы", date="31.12.2021")


if __name__ == '__main__':
    app()
