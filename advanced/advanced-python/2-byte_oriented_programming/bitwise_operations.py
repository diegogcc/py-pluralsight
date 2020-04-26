# bit representation
>>> 0b11110000
240

# decimal to binary
>>> bin(240)
'0b11110000 '

#  XOR
>>> bin(0b11100100 ^ 0b00100111)
'0b11000011'

#  Compliment / NOT
>>> bin(~0b11110000)
'-0b11110001'

# Shift << >>
>>> 1 << 3       # 0001 << 3   ==   0010 << 2   ==   0100 << 1   ==   1000 << 0
8

# Bytewise operations with integers
# get the Byte object representation of a number
# specify the number of bytes to represent it
# spedify the byte order
>>> int(0xcafebabe).to_bytes(length=4, byteorder='big')
b'\xca\xfe\xba\xbe'         # most sifnificant byte first
>>> int(0xcafebabe).to_bytes(length=4, byteorder='little')
b'\xbe\xba\xfe\xca'         # less significant byte first

# From bytes
>>> int.from_bytes(b'\xbe\xba\xfe\xca', byteorder='little')
3405691582
>>> hex(3405691582)
'0xcafebabe'


# Byte oriented representation of an integer using 2 bytes 
# will fail for negative integers (OverflowError)
>>> int(-241).to_bytes(length=2, byteorder='big')
OverflowError: can't convert negative int to unsigned           # unsigned
>>> int(-241).to_bytes(length=2, byteorder='big', signed=True)
b'\xff\x0f'                                                     # signed