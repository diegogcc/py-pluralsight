'''
    filter()
    apply a function to each element in a sequence, constructing
    a new sequence with the elements for which the function returns True
    the function it takes must only accept a single argument.
'''

positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
positives                   # <filter object at 0x10d1d58d0>
list(positives)             # [1, 6, 8]


''' Passing None as the first argument will remove elements
    that evaluate to False.
'''
trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])
list(trues)                 # [1, True, [1, 2, 3], 'hello']