'''
Fraction can represent Rational numbers
'''

from fractions import Fraction
from decimal import Decimal

two_thirds = Fraction(2, 3) # Fraction(2, 3)
print(two_thirds)           # 2/3

try:
    print('Giving Fraction a zero denominator')
    zero_denom = Fraction(4, 0)
except ZeroDivisionError:
    print('Causes a ZeroDivisionError')

Fraction(123049812340988647491287349182374)
# Fraction(123049812340988647491287349182374, 1)

''' Fractions can be constructed from float objects '''
Fraction(0.5)   # Fraction(1, 2)

''' If float cannot be represented by the binary float, results might be unexpected '''
Fraction(0.1)             # Fraction(3602879701896397, 36028797018963968)
Fraction(Decimal('0.1'))  # Fraction(1, 10)

''' Fraction can also (as with Decimal) be constructed from strings '''
Fraction('2/3')     # Fraction(2, 3)

''' Arithmetic is as expected '''
Fraction(2, 3) + Fraction(4, 5)
# Fraction(22, 15)
Fraction(2, 3) - Fraction(4, 5)
# Fraction(-2, 15)
Fraction(2, 3) * Fraction(4, 5)
# Fraction(8, 15)
Fraction(2, 3) / Fraction(4, 5)
# Fraction(5, 6)
Fraction(2, 3) // Fraction(4, 5)
# 0
Fraction(2, 3) % Fraction(4, 5)
# Fraction(2, 3)
