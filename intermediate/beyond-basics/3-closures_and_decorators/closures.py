'''
Local functions can access the enclosing attributes of the containing function
because they are CLOSURES
Closure:    Maintains the reference of objects from earlier scopes
'''

def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()
# closed over

lf.__closure__
# (<cell at 0x10d0bc0d0: str object at 0x10d0b6f70>,)