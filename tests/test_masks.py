import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_number, masked',
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('1234567890123456', '1234 56** **** 3456')])
def test_get_mask_card_number(card_number, masked):
    result = get_mask_card_number(card_number)
    assert (result == masked)


@pytest.mark.parametrize('account_number, masked',
                         [('73654108430135874305', '**4305'),
                          ('12345678901234567890', '**7890'),
                          ('78901234567890123456', '**3456'),
                          ('45678901234567890123', '**0123')])
def test_get_mask_account(account_number, masked):
    result = get_mask_account(account_number)
    assert (result == masked)
