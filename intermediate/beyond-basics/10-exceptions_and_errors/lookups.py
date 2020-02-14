'''
IndexError.mro()
    [<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
KeyError.mro()
    [<class 'KeyError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]

Both IndexError and KeyError are subclasses of LookupError
'''

def lookups_too_specific():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print("Handled IndexError")
    
    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except KeyError:
        print("Handled KeyError")


# This will have the SAME results.
def lookups_general():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print("Handled IndexError")
    
    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")