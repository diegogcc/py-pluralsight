import decimal
from decimal import Decimal

print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, 
# capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

Decimal(5)      # Decimal('5')
Decimal('5')    # Decimal('5')      <- accepts strings

print(0.8 - 0.7)                        # 0.10000000000000009
print(Decimal(0.8) - Decimal(0.7))      # 0.1000000000000000888178419700
print(Decimal('0.8') - Decimal('0.7'))  # 0.1
''' Better use it with strings to avoid inexact results due to convertion
    to base 2 float objects. '''


decimal.getcontext().traps[decimal.FloatOperation] = True
try:
    print('Trying to use Decimal with a float')
    Decimal(0.8)
except decimal.FloatOperation:
    print('Generates decimal.FloatOperation error')


''' Decimal preserves the precision of numbers with trailing zeros. '''
a = Decimal('3')
b = Decimal('3.0')
c = Decimal('3.00')
print(a)    # 3
print(b)    # 3.0
print(c)    # 3.00

''' Decimal also supports special values '''
Decimal('Infinity')
Decimal('-Infinity')
Decimal('NaN')