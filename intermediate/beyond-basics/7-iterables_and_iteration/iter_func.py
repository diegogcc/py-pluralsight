'''
    iter(callable, sentinel)
    can be called on 'callable' until it reaches the value of 'sentinel'
    if sentinel == None: infinite sequence
'''

import datetime

i = iter(datetime.datetime.now, None)
next(i)
# datetime.datetime(2020, 1, 28, 19, 40, 58, 974714)
next(i)
# datetime.datetime(2020, 1, 28, 19, 43, 6, 545894)
next(i)
# datetime.datetime(2020, 1, 28, 19, 43, 7, 297919)
next(i)
# datetime.datetime(2020, 1, 28, 19, 43, 39, 336807)