from src.func import load_operations, get_executed_list, sort_op_list, get_user_msg, represent_date, hide_nums

raw_op_list = load_operations()
ex_op_list = get_executed_list(raw_op_list)
sort_5_oplist = sort_op_list(ex_op_list)

for operation in sort_5_oplist:
    print(get_user_msg(represent_date(operation['date']), hide_nums(operation['to']), hide_nums(operation.get('from')), operation['description'], operation['operationAmount']['amount'], operation['operationAmount']['currency']['name']))
