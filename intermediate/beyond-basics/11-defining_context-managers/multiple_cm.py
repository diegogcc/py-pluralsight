'''
with cm1() as a, cm2() as b:
    BODY

----  OR ----

with cm1() as a:
    with cm2() as b:
        BODY

'''

import contextlib

@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield
    print('Exiting', name)

if __name__ == "__main__":

    ''' Multiple Context Managers'''
    with nest_test('outer'), nest_test('inner'):
        print('BODY')
        # Entering outer
        # Entering inner
        # BODY
        # Exiting inner
        # Exiting outer

    ''' Nested Context Managers '''         # Same result
    with nest_test('outer'):
        with nest_test('inner'):
            print('BODY')
        # Entering outer
        # Entering inner
        # BODY
        # Exiting inner
        # Exiting outer