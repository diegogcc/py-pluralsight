'''
First introspection tool is type()
'''

>> i = 7
>> type(i)                          # <class 'int'>
>> int                              # <class 'int'>
>> repr(int)                        # "<class 'int'>"
type(i) is int                      # True

''' calling the constructor through type '''
>> type(i)(78)                      # 78
''' what type does type() return? '''
>> type(type(i))                    # <class 'type'>


''' type() returns __class__ atr '''
>> i.__class__                      # <class 'int'>
>> i.__class__.__class__            # <class 'type'>
>> i.__class__.__class__.__class__  # <class 'type'>       type is its own type

''' type is an object '''
issubclass(type, object)            # True
''' object is of type "type" '''
type(object)                        # <class 'type'>

'''
Don't use type tests in general
Preferably use 
    issubclass()
    isinstance()
'''