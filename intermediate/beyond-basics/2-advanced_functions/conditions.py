# 1
def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

# 2
def sequence_class(immutable):
    return tuple if immutable else list 