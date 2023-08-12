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
