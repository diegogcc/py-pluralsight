''' list '''
l = [i*2 for i in range(10)]
type(l)         # <class 'list'>
dir(l)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
# 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
l.append(42)
print(l)        # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 42]

''' dict '''
d = {i: i*2 for i in range(10)}
type(d)         # <class 'dict'>
''' set '''
s = {i for i in range(10)}
type(s)         # <class 'set'>
''' generator '''
g = (i for i in range(10))
type(g)         # <class 'generator'>


''' multi-input '''
mult = [(x, y) for x in range(3) for y in range(2)]
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
mult2 = []
for x in range(3):
    for y in range(2):
        mult2.append((x, y))
mult == mult2                       # True

''' multiple clauses '''
values = [x / (x - y) 
          for x in range(100) 
          if x > 50 
          for y in range(100) 
          if x - y != 0]
values2 = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if (x - y) != 0:
                values2.append(x / (x - y))
values == values2                   # True
 