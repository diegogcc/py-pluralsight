def hypervolume(*args):
    print(args)
    print(type(args))

hypervolume(3, 4)
# (3, 4)
# <class 'tuple'>
hypervolume(3, 4, 5)
# (3, 4, 5)
# <class 'tuple'>



def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

hypervolume(3, 4)
# 12
hypervolume(3, 4, 5)
# 60
hypervolume()
# Raises -> StopIteration



def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

hypervolume()
# Raises -> TypeError: hypervolume() missing 1 required positional argument: 'length'



def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))    

tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border=1)
# img
# {'src': 'monet.jpg', 'alt': 'Sunrise by Claude Monet', 'border': 1}
# <class 'dict'>



def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border=1)
# '<img src="monet.jpg" alt="Sunrise by Claude Monet" border="1">'



def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11, 12, 13, 14)

print_args(*t)
# 11
# 12
# (13, 14)



def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha':52}

color(**k)
# r = 21
# g = 68
# b = 120
# {'alpha': 52}



def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
    result = f(*args, **kwargs)
    print("result =", result)
    return result

int("ff", base=16)
# 255

trace(int, "ff", base=16)
# args = ('ff',)
# kwargs = {'base': 16}
# result = 255
# 255

