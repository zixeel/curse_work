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
    if number is None:
        return ''
    elif number.startswith('Счет'):
        return 'Cчёт '+'**'+number[-4:]
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


def represent_date(date):
    """Принимает дату и выводит её в необходимом формате"""
    return date[8:10]+'.'+date[5:7]+'.'+date[:4]


def get_user_msg(formatted_data, formatted_to, formatted_from,description, operationAmount, name):
    """принимает всю форматированю информацию и делает из неё сообщение для пользователя"""
    return f"""{formatted_data} {description} 
{formatted_to} -> {formatted_from}
{operationAmount} {name}
"""
