def filter_by_state(dict_list: list, state='EXECUTED') -> list:
    """Возвращает список, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_dict_list = []
    for dic in dict_list:
        if dic['state'] == state:
            new_dict_list.append(dic)
    return new_dict_list


def sort_by_date(dict_list: list, order='decrease') -> list:
    """Возвращает новый список, отсортированный по дате"""
    if order == 'decrease':
        sorted_dict_list = sorted(dict_list, key=lambda i: (i['date']))
        sorted_dict_list.reverse()
    else:
        sorted_dict_list = sorted(dict_list, key=lambda i: (i['date']))
    return sorted_dict_list
