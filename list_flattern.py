__author__ = 'maryan_partyka'

#lst = [[[0, [[[1, 2], 3], 4],67], [[6, 7]]]]
lst = [1, [2, 3], 4, [[6, 7]]]
new_lst = []


def lst_flattern(lst):
    for item in lst:
        if type(item) is list:
            lst_flattern(item)
        else:
            new_lst.append(item)
    return new_lst

print lst_flattern(lst)
