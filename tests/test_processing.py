import pytest

from processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('dict_list, state, new_dict_list',
                         [([{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          'EXECUTED', [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ([{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          'CANCELED', [{'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])])
def test_filter_by_state(dict_list, state, new_dict_list):
    result = filter_by_state(dict_list, state)
    assert (result == new_dict_list)


@pytest.mark.parametrize('dict_list, order, sorted_dict_list',
                         [([{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          'decrease', [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ([{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          'increase', [{'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                       {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])])
def test_sort_by_date(dict_list, order, sorted_dict_list):
    result = sort_by_date(dict_list, order)
    assert (result == sorted_dict_list)
