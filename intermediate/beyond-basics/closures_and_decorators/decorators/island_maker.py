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
    # Diego
    i = norwegian_island_maker('Diego')
    print(i)
    # Calling <function escape_unicode.<locals>.wrap at 0x1027e4170>
    # 'Diego\xf8y'
    print('Lionel')
    # Lionel
    i = norwegian_island_maker('Lionel')
    print(i)
    # Calling <function escape_unicode.<locals>.wrap at 0x1027e4170>
    # 'Lionel\xf8y'
    print('disabling tracer')
    # disabling tracer
    tracer.enabled = False
    print('Marco')
    # Marco
    i = norwegian_island_maker('Marco')
    print(i)
    # 'Marco\xf8y'
    s = ' Island'
    print('english suffix: {}'.format(s))
    # english suffix:  Island
    im = IslandMaker(s)
    print('Cruyff')
    # Cruyff
    print(im.make_island('Cruyff'))
    # Cruyff Island
