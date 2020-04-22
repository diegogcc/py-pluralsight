'''
For-Else

    for item in iterable:
        if match(item):
            result = item
            break
    else:   #nobreak
        # No match found.
        result = None
'''

'''
Ensuring a list contains at least one integer divisible by a given value.
'''
items = [2, 3, 36, 45, 66, 25]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:   # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))
