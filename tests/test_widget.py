import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('card_number, complete_number',
                         [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 73654108430135874305', 'Счет **4305'),
                          ('Счет 12345678901234567890', 'Счет **7890')])
def test_mask_account_card(card_number, complete_number):
    result = mask_account_card(card_number)
    assert (result == complete_number)


@pytest.mark.parametrize('date_and_time, complete_date',
                         [('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('1999-07-31T02:26:18.671407', '31.07.1999')])
def test_get_date(date_and_time, complete_date):
    result = get_date(date_and_time)
    assert (result == complete_date)
