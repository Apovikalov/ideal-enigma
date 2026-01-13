import pytest

from src.bank_operations import process_bank_operations, process_bank_search


@pytest.mark.parametrize('data, search, new_list',
                         [([{'date': '08.12.2019', 'description': 'Открытие вклада', 'status': 'EXECUTED',
                             'amount': '40542 руб.', 'to': 'Счет **4321'},
                            {'date': '12.11.2019', 'description': 'Перевод с карты на карту', 'status': 'EXECUTED',
                             'amount': '130 USD', 'from': 'MasterCard 7771', 'to': 'Visa Platinum 1293'},
                            {'date': '18.07.2018', 'description': 'Перевод организации', 'status': 'CANCELED',
                             'amount': '8390 руб.', 'from': 'Visa Platinum 7492', 'to': 'Счет **0034'}],
                           'Перевод',
                           [{'date': '12.11.2019', 'description': 'Перевод с карты на карту', 'status': 'EXECUTED',
                             'amount': '130 USD', 'from': 'MasterCard 7771', 'to': 'Visa Platinum 1293'},
                            {'date': '18.07.2018', 'description': 'Перевод организации', 'status': 'CANCELED',
                             'amount': '8390 руб.', 'from': 'Visa Platinum 7492', 'to': 'Счет **0034'}])])
def test_process_bank_search(data, search, new_list):
    result = process_bank_search(data, search)
    assert (result == new_list)


@pytest.mark.parametrize('data, categories, new_list',
                         [([{'date': '08.12.2019', 'description': 'Открытие вклада', 'status': 'EXECUTED',
                             'amount': '40542 руб.', 'to': 'Счет **4321'},
                            {'date': '12.11.2019', 'description': 'Перевод организации', 'status': 'EXECUTED',
                             'amount': '130 USD', 'from': 'MasterCard 7771', 'to': 'Visa Platinum 1293'},
                            {'date': '18.07.2018', 'description': 'Открытие вклада', 'status': 'CANCELED',
                             'amount': '8390 руб.', 'from': 'Visa Platinum 7492', 'to': 'Счет **0034'}],
                           ['Открытие вклада', 'Перевод организации'],
                           {'Открытие вклада': 2, 'Перевод организации': 1}),
                          ([{'date': '08.12.2019', 'description': 'Открытие вклада', 'status': 'EXECUTED',
                             'amount': '40542 руб.', 'to': 'Счет **4321'},
                            {'date': '12.11.2019', 'description': 'Перевод организации', 'status': 'EXECUTED',
                             'amount': '130 USD', 'from': 'MasterCard 7771', 'to': 'Visa Platinum 1293'},
                            {'date': '18.07.2018', 'description': 'Перевод с карты на карту', 'status': 'CANCELED',
                             'amount': '8390 руб.', 'from': 'Visa Platinum 7492', 'to': 'Счет **0034'}],
                           ['Открытие вклада', 'Перевод организации'],
                           {'Открытие вклада': 1, 'Перевод организации': 1})
                          ])
def test_process_bank_operations(data, categories, new_list):
    result = process_bank_operations(data, categories)
    assert (result == new_list)
