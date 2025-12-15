import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency_name, number, transactions, result",
    [
        (
            "USD",
            2,
            [
                {
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                },
                {
                    "id": 142264268,
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}},
                },
                {
                    "id": 142264268,
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}},
                },
            ],
            [
                {
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                },
                {
                    "id": 142264268,
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}},
                },
            ],
        ),
        (
            "RUB",
            1,
            [
                {
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                },
                {
                    "id": 123987645,
                    "operationAmount": {"amount": "2345.67", "currency": {"name": "RUB", "code": "RUB"}},
                },
                {
                    "id": 142264268,
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}},
                },
            ],
            [{"id": 123987645, "operationAmount": {"amount": "2345.67", "currency": {"name": "RUB", "code": "RUB"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions, currency_name, number, result):
    usd_transactions = filter_by_currency(transactions, currency_name)
    complete_list = []
    for _ in range(number):
        complete_list.append(next(usd_transactions))
    assert result == complete_list


@pytest.fixture
def my_func():
    my_list = [{"id": 9397195, "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
               {"id": 1422642, "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}}},
               {"id": 1422642, "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}}}]
    return my_list


def test_filter_by_currency_fixture(my_func):
    usd_transactions = filter_by_currency(my_func, "USD")
    complete_list = []
    for _ in range(2):
        complete_list.append(next(usd_transactions))
    assert complete_list == [
        {"id": 9397195, "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 1422642, "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}}}]


@pytest.mark.parametrize(
    "number, transactions, result",
    [
        (
            2,
            [
                {
                    "id": 939719570,
                    "description": "Перевод организации",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                },
                {
                    "id": 142264268,
                    "description": "Перевод со счета на счет",
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}},
                },
                {
                    "id": 142264268,
                    "description": "Перевод с карты на карту",
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}},
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        (
            3,
            [
                {
                    "id": 939719570,
                    "description": "Перевод с карты на карту",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                },
                {
                    "id": 123987645,
                    "description": "Перевод со счета на счет",
                    "operationAmount": {"amount": "2345.67", "currency": {"name": "RUB", "code": "RUB"}},
                },
                {
                    "id": 142264268,
                    "description": "Перевод организации",
                    "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}},
                },
            ],
            ["Перевод с карты на карту", "Перевод со счета на счет", "Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions(transactions, number, result):
    usd_transactions = transaction_descriptions(transactions)
    complete_list = []
    for _ in range(number):
        complete_list.append(next(usd_transactions))
    assert result == complete_list


@pytest.fixture
def my_func_2():
    my_list = [{"id": 939719570,
                "description": "Перевод организации",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
               {"id": 142264268,
                "description": "Перевод со счета на счет",
                "operationAmount": {"amount": "7914.93", "currency": {"name": "RUB", "code": "RUB"}}},
               {"id": 142264268,
                "description": "Перевод с карты на карту",
                "operationAmount": {"amount": "7914.93", "currency": {"name": "USD", "code": "USD"}}}]
    return my_list


def test_transaction_descriptions_fixture(my_func_2):
    usd_transactions = transaction_descriptions(my_func_2)
    complete_list = []
    for _ in range(2):
        complete_list.append(next(usd_transactions))
    assert complete_list == ["Перевод организации", "Перевод со счета на счет"]


@pytest.mark.parametrize(
    "start, end, result",
    [
        (1, 5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ]),
        (357, 362,
            [
                "0000 0000 0000 0357",
                "0000 0000 0000 0358",
                "0000 0000 0000 0359",
                "0000 0000 0000 0360",
                "0000 0000 0000 0361",
                "0000 0000 0000 0362",
            ]),
        (999, 1000, ["0000 0000 0000 0999", "0000 0000 0000 1000"]),
        (1234567888, 1234567890, ["0000 0012 3456 7888", "0000 0012 3456 7889", "0000 0012 3456 7890"]),
    ],
)
def test_card_number_generator(start, end, result):
    card_numbers = card_number_generator(start, end)
    complete_list = []
    for _ in range(start, end + 1):
        complete_list.append(next(card_numbers))
    assert result == complete_list


@pytest.fixture
def my_func_3():
    start_and_end = (8, 9)
    return start_and_end


def test_card_number_generator_fixture(my_func_3):
    card_numbers = card_number_generator(my_func_3[0], my_func_3[1])
    complete_list = []
    for _ in range(my_func_3[0], my_func_3[1] + 1):
        complete_list.append(next(card_numbers))
    assert complete_list == ["0000 0000 0000 0008", "0000 0000 0000 0009"]
