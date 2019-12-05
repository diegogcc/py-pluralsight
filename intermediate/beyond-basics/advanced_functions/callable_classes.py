def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

if __name__ == '__main__':
    seq = sequence_class(immutable=True)
    t = seq("this is a tuple")
    
    print(t)
    # ('t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'u', 'p', 'l', 'e')

    seq = sequence_class(immutable=False)
    l = seq("this is a list")
    # ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'l', 'i', 's', 't']
