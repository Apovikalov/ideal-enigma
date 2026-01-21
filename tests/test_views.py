import unittest
from typing import Any
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.views import (greeting_time, calculate_total_expenses, for_each_card,
                       top_5_transactions, get_price_stock, read_xlsx)


@pytest.mark.parametrize('date_and_time, greet',
                         [('2024-03-11 02:26:18', 'Доброй ночи!'),
                          ('1999-07-31 07:26:18', 'Доброе утро!'),
                          ('1999-07-31 15:26:18', 'Добрый день!'),
                          ('1999-07-31 22:26:18', 'Добрый вечер!')])
def test_greeting_time(date_and_time, greet):
    result = greeting_time(date_and_time)
    assert (result == greet)

@pytest.mark.parametrize('transactions_sum, total_expenses',
                         [([{'name': '1', 'Сумма платежа': -2.3},
                            {'name': '2', 'Сумма платежа': -5.3}], 7.6),
                          ([{'name': '1', 'Сумма платежа': -8},
                            {'name': '2', 'Сумма платежа': 6},
                            {'name': '3', 'Сумма платежа': -9}], 17.0)])
def test_calculate_total_expenses(transactions_sum, total_expenses):
    result = calculate_total_expenses(transactions_sum)
    assert (result == total_expenses)

@patch("requests.get")
def mocked_requests_get(*args: Any) -> Any:
    """Заглушка для запросов к API.
    Возвращает моковый ответ с курсом RUB к USD, если timeout = 15,
    иначе возвращает пустой ответ.
    """

    class MockResponse:
        def __init__(self, json_data: Any, status_code: Any) -> None:
            self.json_data = json_data
            self.status_code = status_code

        def json(self) -> Any:
            return self.json_data

    if args[0].timeout == 15:
        return MockResponse({"rates": {"RUB": 70}}, 200)
    else:
        return MockResponse({}, 404)


# class TestFunctions(unittest.TestCase):
    """Тестовый класс для функций из src.views."""

    def setUp(self) -> None:
        """Настройка перед тестом."""
        pass

    @patch("yfinance.Ticker")
    def test_get_stock_currency(self, mock_ticker: Any) -> None:
        """Проверяет работу функции get_stock_cur, получающей акции с помощью Yahoo Finance."""
        mock_data = Mock()
        mock_data.history.return_value = pd.DataFrame({"High": [100]})
        mock_ticker.return_value = mock_data
        self.assertEqual(get_price_stock("AAPL"), 100)
