class NoBinding:

    def __init__(self):
        self.message = 'global'

    def enclosing(self):
        message = 'enclosing'

        def local():
            message = 'local'

        print('enclosing message: ', message)
        local()
        print('enclosing message: ', message)
    
    def print_scopes(self):
        print('global message: ', message)
        self.enclosing()
        print('global message: ', message)

    # global message:  global
    # enclosing message:  enclosing
    # enclosing message:  enclosing
    # global message:  global

class GlobalBinding:
    def __init__(self):
        self.message = 'global'  

    def enclosing(self):
        message = 'enclosing'

        def local():
            global message
            message = 'local'

        print('enclosing message: ', message)
        local()
        print('enclosing message: ', message)
    
    def print_scopes(self):
        print('global message: ', message)
        self.enclosing()
        print('global message: ', message)
    
    # global message:  global
    # enclosing message:  enclosing
    # enclosing message:  enclosing
    # global message:  local

class NonLocal:
    def __init__(self):
        self.message = 'global'  

    def enclosing(self):
        message = 'enclosing'

        def local():
            nonlocal message
            message = 'local'

        print('enclosing message: ', message)
        local()
        print('enclosing message: ', message)
    
    def print_scopes(self):
        print('global message: ', message)
        self.enclosing()
        print('global message: ', message)
    
    # global message:  global
    # enclosing message:  enclosing
    # enclosing message:  local
    # global message:  global

if __name__ == '__main__':
    message = 'global'
    # dc = NoBinding()
    # dc = GlobalBinding()
    dc = NonLocal()
    dc.print_scopes()
