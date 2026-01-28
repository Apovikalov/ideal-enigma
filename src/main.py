import json
import logging
from datetime import datetime
from pathlib import Path

from src.utils import read_xlsx
from src.views import filter_by_date, for_each_card, get_price_stock, greeting_time, top_5_transactions

# from src.views import calculate_total_expenses, currency_rates

logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler("main.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
data_frame = read_xlsx(file_path)
# data_frame = read_excel("../data/operations.xlsx")


def main(date: str):
    """Функция создающая JSON ответ для страницы главная"""
    logger.info("Начало работы главной функции (main)")
    final_list = filter_by_date(date, "../data/operations.xlsx")
    greeting = greeting_time(datetime.now())
    cards = for_each_card(final_list)
    top_trans = top_5_transactions(final_list)
    stocks_prices = get_price_stock(["AAPL"])
    # currency_r = currency_rates(["USD", "EUR"])
    logger.info("Создание JSON ответа")
    result = [{
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_trans,
        # "currency_rates": currency_r,
        "stock_prices": stocks_prices,
    }]
    date_json = json.dumps(
        result,
        indent=4,
        ensure_ascii=False,
    )
    logger.info("Завершение работы главной функции (main)")
    return date_json
