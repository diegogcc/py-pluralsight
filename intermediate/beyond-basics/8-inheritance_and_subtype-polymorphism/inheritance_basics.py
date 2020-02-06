class Base:
    def __init__(self):
        print('Base initializer')
    
    def f(sefl):
        print('Base.f()')

class SubNoInit(Base):
    def f(self):
        print('SubNoInit.f()')

class SubInit(Base):
    def __init__(self):
        super.__init__()
        print('SubInit initializer')

    def f(self):
        print('SubInit.f()')

if __name__ == "__main__":
    b = Base()
    # Base initializer
    b.f()
    # Base.f()

    s = SubNoInit()
    # Base initializer
    s.f()
    # SubNoInit.f()

    si = SubInit()
    # Base initializer
    # SubInit initializer
    si.f()
    # SubInit.f()
