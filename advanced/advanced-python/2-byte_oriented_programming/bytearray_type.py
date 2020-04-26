'''
    byte sequence - immutable
    bytearray sequenc - mutable

'''
# Construction of an empty bytearray
>>> bytearray()
bytearray(b'')

# Construction of a bytearray containing a given number of 0 bytes
>>> bytearray(5)
bytearray(b'\x00\x00\x00\x00\x00')

# Construction from another sequence of bytes (like bytes object)
>>> bytearray(b'Construct from a sequence of bytes')
bytearray(b'Construct from a sequence of bytes')

# Construction form an unicode string, supplying an encoding
>>> bytearray('Characters Å and Ø', 'utf16')
bytearray(b'\xff\xfeC\x00h\x00a\x00r\x00a\x00c\x00t\x00e\x00r\x00s\x00 \x00\xc5\x00 \x00a\x00n\x00d\x00 \x00\xd8\x00')

# Using fromhex name constructor, a stirng containgin concatenated 2-digit hex numbers
>>> bytearray.fromhex('54686520717569636b2062726f776e20666f78')
bytearray(b'The quick brown fox')


# Mutating the array
>>> pangram = bytearray(b'The quick brown fox')
>>> pangram.extend(b' jumps over the lazy dog')
bytearray(b'The quick brown fox jumps over the lazy dog')

>>> pangram[40:43] = b'god'
bytearray(b'The quick brown fox jumps over the lazy god')

>>> pangram.upper()
bytearray(b'THE QUICK BROWN FOX JUMPS OVER THE LAZY GOD')

>>> words = pangram.split()
[bytearray(b'The'), bytearray(b'quick'), bytearray(b'brown'), bytearray(b'fox'), bytearray(b'jumps'), bytearray(b'over'), bytearray(b'the'), bytearray(b'lazy'), bytearray(b'god')]

>>> bytearray(b' ').join(words)
bytearray(b'The quick brown fox jumps over the lazy god')
