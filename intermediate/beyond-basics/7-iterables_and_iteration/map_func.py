''' 
    map() is a tool of functional programming.
    pass a function and a list of arguments.
    returns a list of results when called.
'''

# Trace class to show when map() is being called
class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

map(ord, 'The quick brown fox')     # <map object at 0x10d1ccf10>


''' Using Trace for manual evaluation '''
result = map(Trace()(ord), 'The quick brown fox')
next(result)
# Calling <built-in function ord>
# 84
next(result)
# Calling <built-in function ord>
# 104
next(result)
# Calling <built-in function ord>
# 101

''' Using a list or a for loop '''
l = list(map(ord, 'The quick brown fox'))
# [84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110, 32, 102, 111, 120]
for o in map(ord, 'The quick brown fox'):
    print(o)
# 84
# 104
# 101
# 32
# 113
# …


''' Multiple inputs '''
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']
def combine(size, color, animal):
    return '{} {} {}'.format(size, color, animal)

m = list(map(combine, sizes, colors, animals))
# ['small lavender koala', 'medium teal platypus', 'large burnt orange salamander']


''' map() vs. comprehensions '''
[str(i) for i in range(4)]
# ['0', '1', '2', '3']
list(map(str, range(4)))
# ['0', '1', '2', '3']

i = (srt(i) for i in range(4))
list(i)
# ['0', '1', '2', '3']
i = map(str, range(4))
list(i)
# ['0', '1', '2', '3']
