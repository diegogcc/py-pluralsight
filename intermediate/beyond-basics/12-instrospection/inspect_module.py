>> import inspect
>> import sorted_set

>> inspect.ismodule(sorted_set)
# True
>> inspect.getmembers(sorted_set)
# [('Sequence', <class 'collections.abc.Sequence'>), 
# ('Set', <class 'collections.abc.Set'>), 
# ('SortedSet', <class 'sorted_set.SortedSet'>), 
# ...,
# ...,
# ...]

>> inspect.getmembers(sorted_set, inspect.isclass)
# [('Sequence', <class 'collections.abc.Sequence'>), ('Set', <class 'collections.abc.Set'>), 
# ('SortedSet', <class 'sorted_set.SortedSet'>), ('chain', <class 'itertools.chain'>)]

''' as the 'sorted_set' module imported 'itertools.chain', these are the same: '''
>> from itertools import chain
>> from sorted_set import chain