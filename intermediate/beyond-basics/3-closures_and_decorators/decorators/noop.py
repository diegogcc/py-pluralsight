# functools.wraps()
import functools

def noop_func(f):
    @functools.wraps(f)    # <------------------
    def noop_wrapper():
        return f()
    return noop_wrapper
    
def noop_no_func(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

def hello():
    '''Print a well-known message.'''
    print('Hello, world!')

@noop_no_func
def ciao():
    '''Print a well-known message.'''
    print('Ciao, mondo!')

@noop_func
def hola():
    '''Print a well-known message.'''
    print('Hola, mundo!')

if __name__ == "__main__":
    print(hello.__name__)  # hello 
    print(hello.__doc__)  # Print a well-known message.
    
    print(ciao.__name__)  # noop_wrapper
    print(ciao.__doc__)  # None
    
    print(hola.__name__)  # hola
    print(hola.__doc__)  # Print a well-known message.

