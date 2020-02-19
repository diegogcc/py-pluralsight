import contextlib

@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, 'received and exception')
        if propagate:               # can be configured to propagate or swallow exceptions
            raise

if __name__ == "__main__":

    ''' The outer cm won't see the exception '''
    with propagater('outer', True), propagater('inner', False):
        raise ValueError("Something went wrong")
        # inner received and exception
        # outer exited normally   

    ''' The inner propagates and the outer one swallows exceptions '''
    with propagater('outer', False), propagater('inner', True):
        raise ValueError("Something went wrong")
        # inner received and exception
        # outer received and exception

    ''' Exception is propagated '''
    with propagater('outer', True), propagater('inner', True):
        raise ValueError("Something went wrong")
        # inner received and exception
        # outer received and exception
        # Traceback (most recent call last):
        # File "<stdin>", line 2, in <module>
        # ValueError: Something went wrong