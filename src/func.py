import json
import os


def load_operations():
    """Загружает список операций из джейсон файла в пайтон список"""
    with open(os.path.join('../data', 'operations.json'), "r", encoding="utf-8") as f:
        operations_list = json.load(f)
        return operations_list


def get_executed_list(operation_list):
    """возвращает список executed операций"""
    all_executed_op = []
    for operation in operation_list:
        if operation.get('state') and operation['state'] == 'EXECUTED':
            all_executed_op.append(operation)
    return all_executed_op


# def get_date(operation):
# """"ДЛЯ ПОНИМАНИЯ"""
#     return operation['date']


def sort_op_list(op_list):
    return sorted(op_list, key=lambda operation: operation['date'], reverse=True)[:5]












# data = load_operations()
# data_ex = get_executed_list(data)
# print(sort_op_list(data_ex))


# def sut(x):
#     return x*5
# lambda x: x*5

