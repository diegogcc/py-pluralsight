''' 
Assertions:
    means to monitor PROGRAM INVARIANTS
        Invariants:     conditions that should always be True
'''

def modulus_three(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:       # r == 2
        print("Remainder 2")

def modulus_three_fixed(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:    
        assert r == 2, "Remainder is not 2!"
        print("Remainder 2")

def modulus_three_alternative(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Remainder 2")
    else:
        assert False, "This should never happen!"
