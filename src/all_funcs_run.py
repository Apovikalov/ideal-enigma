from pathlib import Path

from src.reports import spending_by_category
from src.services import simple_search
from src.utils import read_xlsx
from src.views import (calculate_total_expenses, filter_by_date, for_each_card, get_price_stock, greeting_time,
                       top_5_transactions)

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
my_list = read_xlsx(file_path)


def run_all_functions():
    """Запускает все функции из модулей views, reports, services"""
    greeting = greeting_time(None)
    expenses = calculate_total_expenses(my_list)
    each_card = for_each_card(my_list)
    top_5 = top_5_transactions(my_list)
    stock_price = get_price_stock(["AAPL"])
    fbd = filter_by_date("", "../data/operations.xlsx")
    spend = spending_by_category(my_list, "Переводы", date="31.12.2021")
    search = simple_search(my_list, "Ozon.ru")
    for i in [greeting, expenses, each_card, top_5, stock_price, fbd, spend, search]:
        print(i)


run_all_functions()
