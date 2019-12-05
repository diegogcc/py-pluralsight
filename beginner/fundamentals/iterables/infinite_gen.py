def lucas():
    '''A series that starts with 2 and 1 and every value afterwards is 
    the sum of the two preceding values.
    '''
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b
        