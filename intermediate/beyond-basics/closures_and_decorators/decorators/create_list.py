'''Decorators can also be used to validating function arguments'''

def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value] * size
    

if __name__ == "__main__":
    a = create_list('a', 3)
    print(a)    
    # ['a', 'a', 'a']
    b = create_list('b', 0)
    print(b)
    # []
    c = create_list('c', -1)
    # Traceback (most recent call last):
    #   File "create_list.py", line 23, in <module>
    #       c = create_list('c', -1)
    #   File "create_list.py", line 8, in wrap
    #       'Argument {} must be non-negative.'.format(index))
    # ValueError: Argument 1 must be non-negative.
    print(c)
    # 