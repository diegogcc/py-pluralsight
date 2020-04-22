'''
A normal Try clause:
    try:
        # This code might raise and exception
        do_something()
        do_something_else()
    except ValueError:
        # ValueError caught and handled
        handle_value_error()

The problem is that we don't know if do_something() or do_something_else()
raised the exception:
Try_Else:
    
    try:
        # This code might raise an exception
        do_something()
    except ValueError:
        # ValueError caught and handled
        handle_value_error()
    else:
        # No exception was raised
        # We know that do_something() succeded, so:
        do_something_else()

A 'finally' clause can also be added. 
The 'else' clauase will execute only if there was NO exception.
The 'finally' clause will always execute.
'''

try:
    f = open("filename.txt", 'r')
except OSError:     # OSError replaces IOError from Python 3.3 onwards
    print("File could not be opened for read")
else:
    # Now we are sure the file is open
    print("Number of lines", sum(1 for line in f))
    f.close()