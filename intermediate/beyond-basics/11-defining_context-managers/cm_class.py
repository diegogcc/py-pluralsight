
class LoggingContextManager:
    def __enter__(self):
        print("LogginContextManager.__enter__()")
        return "You are in a with-block!: {}".format(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManager.__exit__:"
                  "normal exit detected.")
        else:
            print("LoggingContextManager.__exit__:"
                  "Exception detected!"
                  "type={}, value={}, traceback={}".format(
            exc_type, exc_val, exc_tb))
        

if __name__ == "__main__":
    ''' Normal exit '''
    with LoggingContextManager() as x:
        print(x)
        # LogginContextManager.__enter__()
        # You are in a with-block!: <__main__.LoggingContextManager object at 0x105403510>
        # LoggingContextManager.__exit__:normal exit detected.

    ''' Exceptional exit '''
    with LoggingContextManager() as x:
        raise ValueError('Something has gone wrong!')
        print(x)
        # LogginContextManager.__enter__()
        # LoggingContextManager.__exit__:Exception detected!type=<class 'ValueError'>, value=Something has gone wrong!, traceback=<traceback object at 0x101931550>
        # Traceback (most recent call last):
        #   File "example1.py", line 27, in <module>
        #     raise ValueError('Something has gone wrong!')
        # ValueError: Something has gone wrong!

    ''' Exception propagation 
            if  __exit__()  returns False, the exception is propagated
    '''
    try:
        with LoggingContextManager():
            raise ValueError("The system is down")
    except ValueError:
        print('*** ValueError detected ***')
    # LogginContextManager.__enter__()
    # LoggingContextManager.__exit__:Exception detected!type=<class 'ValueError'>, value=The system is down, traceback=<traceback object at 0x10ad83410>
    # *** ValueError detected ***