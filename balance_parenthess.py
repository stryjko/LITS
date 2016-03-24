__author__ = 'maryan_partyka'

input_str = '[()], (([3,4])), (6,7,8)'
all_parentheses = [['(', ')'], ['[', ']'], ['{', '}']]


def balance_parentheses(input_str):
    temp_lst = []
    for index, item in enumerate(input_str):
        for parentheses in all_parentheses:
            if item == parentheses[0]:
                temp_lst.append(item)
            elif item == parentheses[1] and len(temp_lst) != 0 and temp_lst[-1] == parentheses[0]:
                temp_lst.pop(-1)
            elif item == parentheses[1] and (len(temp_lst) == 0 or temp_lst[-1] != parentheses[0]):
                return False
            else:
                pass

    return True if len(temp_lst) == 0 else False

print balance_parentheses(input_str)
