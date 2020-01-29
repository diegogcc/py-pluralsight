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
# mul 1 2
# mul 2 3
# mul 6 4
# mul 24 5
# mul 120 6
# mul 720 7
# mul 5040 8
# mul 40320 9
# 362880

''' initial value '''
values = [1, 2, 3]
reduce(operator.add, values, 0)
# 6
reduce(operator.add, values, 10)
# 16
