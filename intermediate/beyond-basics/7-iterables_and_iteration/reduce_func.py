'''
    functools.reduce()
    repeatedly apply a function to the elements of a sequence,
    reducing them to a single value
'''

from functools import reduce
import operator

reduce(operator.add, [1, 2, 3, 4, 5])
# 15

def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x * y

reduce(mul, range(1, 10))