__author__ = 'maryan_partyka'

def own_print(item):
    def inner_function(arg):
        return item + ' it\'s ' + arg
    return inner_function

func = own_print('foo')
print func
print func('bar')
