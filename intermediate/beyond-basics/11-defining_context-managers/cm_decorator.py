''' 
Rewrite example1 using now 
contextlib.contextmanager decorator
'''

import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())

@contextlib.contextmanager
def logging_context_manager_with_propagation():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())
        raise                           # <--- add this line to propagate exceptions
        
if __name__ == "__main__":
    ''' Normal exit '''
    with logging_context_manager() as x:
        print(x)
        # logging_context_manager: enter
        # You are in a with-block!
        # logging_context_manager: normal exit
    
    ''' Exceptional exit
            (Exceptions don't get propagated so they have to be explicitly handled)
    '''
    with logging_context_manager() as x:
        raise ValueError("Something has gone wrong!")
        print(x)
        # logging_context_manager: enter
        # logging_context_manager: exceptional exit (<class 'ValueError'>, ValueError('Something has gone wrong!'), <traceback object at 0x1093b7370>)        

    ''' Exception propagation '''
    with logging_context_manager_with_propagation() as x:
        raise ValueError("Something has gone wrong!")
        print(x)
        # logging_context_manager: enter
        # logging_context_manager: exceptional exit (<class 'ValueError'>, ValueError('Something has gone wrong!'), <traceback object at 0x10cf62640>)
        # Traceback (most recent call last):
        # File "example2.py", line 49, in <module>
        #     raise ValueError("Something has gone wrong!")
        # ValueError: Something has gone wrong!