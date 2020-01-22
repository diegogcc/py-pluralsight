from decimal import Decimal
from fractions import Fraction

''' abs() '''

abs(5)                   # 5
abs(-5.0)                # 5.0
abs(Decimal('-5'))       # Decimal('5')
abs(Fraction(-5, 1))     # Fraction(5, 1)
abs(complex(0, -5))      # 5.0


''' round() '''

round(0.2812, 3)         # 0.281
round(0.625, 1)          # 0.6
round(1.5)               # 2
round(2.5)               # 2     <-    rounds towards even numbers

round(Decimal('3.255'), 1)      # Decimal('3.2')
round(Fraction(57, 100), 2)     # Fraction(57, 100)
round(Fraction(57, 100), 1)     # Fraction(3, 5)
round(Fraction(57, 100), 0)     # Fraction(1, 1)
