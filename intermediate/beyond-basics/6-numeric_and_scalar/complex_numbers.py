''' Python supports complex numbers with "j" '''

a = 3 + 4j      
print(a)        # (3+4j)

print(type(a))
# <class 'complex'>

complex(3)
# (3+0j)
complex(-2, 3)
# (-2+3j)
complex('(-2+3j)')
# (-2+3j)

c = 3 + 5j
print('c = 3 + 5j')
print('c.real = {}'.format(c.real))     # 3.0
print('c.imag = {}'.format(c.imag))     # 5.0
conj = c.conjugate()
print('c.conjugate = {}'.format(conj))  # (3-5j)


''' there is a "cmath" module for mathematic operations '''
try:
    import math
    print('using "math" module for complex numbers')
    math.sqrt(-1)
except ValueError:
    print('produces a ValueError')

import cmath
print('using "cmath" module, can operate complex numbers')
print('cmath.sqrt(-1)')
print(cmath.sqrt(-1))       # 1j


''' "cmath" can also convert to polar '''
c = 1 + 1j
print('phase = {}'.format(cmath.phase(c)))  # 0.7853981633974483
print('magnitude = {}'.format(abs(c)))      # 1.4142135623730951
cmath.polar(c)          # (1.4142135623730951, 0.7853981633974483)
magnitude, phase = cmath.polar(c) 
print(magnitude)        # 1.4142135623730951
print(phase)            # 0.7853981633974483