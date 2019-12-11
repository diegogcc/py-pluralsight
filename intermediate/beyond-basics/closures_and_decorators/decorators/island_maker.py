'''User multiple decorators'''

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix
    
    @tracer
    def make_island(self, name):
        return name + self.suffix


if __name__ == "__main__":
    print('Diego')
    i = norwegian_island_maker('Diego')
    print(i)
    print('Lionel')
    i = norwegian_island_maker('Lionel')
    print(i)
    print('disabling tracer')
    tracer.enabled = False
    print('Marco')
    i = norwegian_island_maker('Marco')
    print(i)

    s = ' Island'
    print('english suffix: {}'.format(s))
    im = IslandMaker(s)
    print('Cruyff')
    print(im.make_island('Cruyff'))

