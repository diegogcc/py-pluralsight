'''
Alternative to a For-Else clause
Extracting the loop into a named function
    - easier to understand
    - easier to test
    - reusable

'''

def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor


items = [2, 3, 36, 45, 66, 25]
divisor = 12

dividend = ensure_has_divisible(items, divisor)

print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))
