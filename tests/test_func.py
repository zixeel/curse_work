import pytest
from src import func


def test_get_executed_list():
    op_list = [{"state": "EXECUTED"},
{"state": "PENDING"},
{"state": "EXECUTED"},
{"state": "CANCELLED"}]
    assert func.get_executed_list(op_list) == [{"state": "EXECUTED"},{"state": "EXECUTED"}]


def test_sort_op_list():
    op_list = [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}, {"date": "2018-06-30T02:08:58.425572"}]
    assert func.sort_op_list(op_list) == [{'date': '2019-08-26T10:50:58.294041'}, {'date': '2019-07-03T18:35:29.512364'}, {'date': '2018-06-30T02:08:58.425572'}]


def test_hide_nums():
    assert func.hide_nums('Visa Classic 2842871111119012') == 'Visa Classic 2842 87** **** 9012'
    assert func.hide_nums('Счет 72731966109147704472') == 'Cчёт **4472'
    assert func.hide_nums('Visa Platinum 2842871111119012') == 'Visa Platinum 2842 87** **** 9012'
    assert func.hide_nums('MasterCard 2842871111119012') == 'MasterCard 2842 87** **** 9012'
    assert func.hide_nums('Maestro 2842871111119012') == 'Maestro 2842 87** **** 9012'
    assert func.hide_nums('МИР 2842871111119012') == 'МИР 2842 87** **** 9012'


def test_represent_date():
    assert func.represent_date("2018-04-04T17:33:34.701093") == '04.04.2018'
    assert func.represent_date('') == '..'

