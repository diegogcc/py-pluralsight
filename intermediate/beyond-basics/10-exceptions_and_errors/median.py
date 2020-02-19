'''
Exception Payloads 
'''

def median(iterable):
    '''Obtain the central value of a series.

    Sorts the iterable and returns the middle value if there is an even
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements.

    Args:
        iterable: A series of orderable items.
    
    Returns:
        the median value.
    '''
    items = sorted(iterable)
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0 
    
def median_len_check(iterable):
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() arg is an empty sequence")
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0 

def main():
    try:
        median_len_check([])
    except ValueError as e:
        print("Payload:", e.args)       # Payload: ('median() arg is an empty sequence',)

if __name__ == "__main__":
    median([5, 2, 1, 4, 3])             # 3
    median([5, 2, 1, 4, 3, 6])          # 3.5

    ''' Exception: '''
    try:
        median([])
    except IndexError as e:
        print(repr(e))                  # IndexError('list index out of range')
    
    try:
        median_len_check([])
    except ValueError as e:
        print("Payload:", e.args)       # Payload: ('median() arg is an empty sequence',)
        print(repr(e))                  # ValueError('median() arg is an empty sequence')

    ''' Example with unicode '''
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(repr(e))                  # UnicodeDecodeError('utf-8', b'\x81', 0, 1, 'invalid start byte')
        print("encoding:", e.encoding)  # encoding: utf-8
        print("reason:", e.reason)      # reason: invalid start byte
        print("object:", e.object)      # object: b'\x81'
        print("start:", e.start)        # start: 0
        print("end:", e.end)            # end: 1