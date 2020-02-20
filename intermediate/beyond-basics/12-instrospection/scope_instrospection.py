''' 
2 built-in functions to examining the content of scopes
'''
>> globals()
# {'__name__': '__main__', '__doc__': None, '__package__': None, 
# '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, 
# '__builtins__': <module 'builtins' (built-in)>}
>> a = 42
>> globals()
''' now the variable a is included '''
# {'__name__': '__main__', '__doc__': None, '__package__': None, 
# '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, 
# '__builtins__': <module 'builtins' (built-in)>, 'a': 42}


''' globals() isn't a representation, is the global namespace '''
>> globals()['tau'] = 78        # Creating a new key and assigning to it
>> tau                          # 78



>> locals()
>>  def report_scope(arg):
...     from pprint import pprint as pp
...     x = 496
...     pp(locals(), width=10)
>> report_scope(42)
# {'arg': 42,
#  'pp': <function pprint at 0x10bce3440>,
#  'x': 496}
>> name = 'Joe Bloggs'
>> age = 28
>> country = 'New Zealand'

>> "{name} is {age} years old and is from {country}".format(**locals())
# 'Joe Bloggs is 28 years old and is from New Zealand'