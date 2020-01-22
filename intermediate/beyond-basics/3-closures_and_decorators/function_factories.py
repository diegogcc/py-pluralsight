def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
square(3) # 9
square(5) # 25

cube = raise_to(3)
cube(3) # 27
cube(5) # 125