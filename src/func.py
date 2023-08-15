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
    """Принимает список екзекьютед операций сортирует их по дате и выводит последние 5"""
    return sorted(op_list, key=lambda operation: operation['date'], reverse=True)[:5]


def hide_nums(number):
    """Принимает номер счёт отправителя определяет какая это карта или счёт и москирует данные на выходе в соответсвии с требованиями курсовой"""
    if number.startswith('Счет'):
        return '**'+number[-4:]
    elif number.startswith('Visa Platinum'):
        number = number.replace('Visa Platinum ', '')
        return 'Visa Platinum' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]
    elif number.startswith('Visa Classic'):
        number = number.replace('Visa Classic ', '')
        return 'Visa Classic' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]
    elif number.startswith('MasterCard'):
        number = number.replace('MasterCard ', '')
        return 'MasterCard' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]
    elif number.startswith('Maestro'):
        number = number.replace('Maestro ', '')
        return 'Maestro' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]
    elif number.startswith('Visa Gold'):
        number = number.replace('Visa Gold ', '')
        return 'Visa Gold' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]
    elif number.startswith('МИР'):
        number = number.replace('МИР ', '')
        return 'МИР' + ' ' + number[0:4] + " " + number[4:6] + '**' + ' ' + '****' + ' ' + number[-4:]





