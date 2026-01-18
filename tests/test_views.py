import pytest

from src.views import greeting_time, calculate_total_expenses


@pytest.mark.parametrize('date_and_time, greet',
                         [('2024-03-11 02:26:18', 'Доброй ночи!'),
                          ('1999-07-31 07:26:18', 'Доброе утро!'),
                          ('1999-07-31 15:26:18', 'Добрый день!'),
                          ('1999-07-31 22:26:18', 'Добрый вечер!')])
def test_greeting_time(date_and_time, greet):
    result = greeting_time(date_and_time)
    assert (result == greet)

@pytest.mark.parametrize('transactions_sum, total_expenses',
                         [([{'name': '1', 'transaction_amount': -2.3},
                            {'name': '2', 'transaction_amount': -5.3}], 7.6),
                          ([{'name': '1', 'transaction_amount': -8},
                            {'name': '2', 'transaction_amount': 6},
                            {'name': '3', 'transaction_amount': -9}], 17.0)])
def test_calculate_total_expenses(transactions_sum, total_expenses):
    result = calculate_total_expenses(transactions_sum)
    assert (result == total_expenses)