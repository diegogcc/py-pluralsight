'''
The default python's source coding is UTF-8
    the characters used in a literal byte string are restricted
    to printable 7-bit ASCII characters (from 0 to 127)
'''

>>> b"This is OK because it's 7-bit ASCII"
b"This is OK because it's 7-bit ASCII"

>>> b"Norwegian characters like Å and Ø are not 7-bit ASCII"
SyntaxError: bytes can only contain ASCII literal characters.

# To represent other bytes with values equivalent to ASCII control codes 
# and byte values from 128 to 255 we use \x
>>> b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII"
b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII"

>>> norsk = b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII"
>>> norsk.decode('latin1')
'Norwegian characters like Å and Ø are not 7-bit ASCII'


# Bytes object index 
# returns an int object NOT a 1-byte sequence
>>> norsk[0]
78
# Bytes object index slicing 
# returns a new bytes object
>>> norsk[21:25]
b'like'


# Create a 0-length byte sequence
>>> bytes()
b''
# Create a 0-filled sequence of bytes 
>>> bytes(5)
b'\x00\x00\x00\x00\x00'
# Pass an iterable series of integers
>>> bytes(range(65, 65+26))
b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Values should always be non-negative and less than 256
>>> bytes([65, 74, 511])
ValueError: bytes must be in range(0, 256)


# To accept unicode characters we can specify also the encoding
>>> bytes("Norwegian characters like Å and Ø", "utf16")
b'\xff\xfeN\x00o\x00r\x00w\x00e\x00g\x00i\x00a\x00n\x00 \x00c\x00h\x00a\x00r\x00a\x00c\x00t\x00e\x00r\x00s\x00 \x00l\x00i\x00k\x00e\x00 \x00\xc5\x00 \x00a\x00n\x00d\x00 \x00\xd8\x00'

# Creating a bytes object from a string consisting of a concatenated, 2-digit, hex numbers
>>> bytes.fromhex('54686520717569636b2062726f776e20666f78')
b'The quick brown fox'

# To go the other direction (str to hex) there isn't a method so:
>>> ''.join(hex(c)[2:] for c in b'The quick brown fox')     # generator to convert each byte into its hex representation and slicing the 0-lead
'54686520717569636b2062726f776e20666f78'
