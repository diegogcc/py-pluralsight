'''                Iteration Protocols

ITERABLE PROTOCOL 

Iterable objects can be passed to the built-in 
iter()
function to get an iterator

iterator = iter(iterable)



ITERATOR PROTOCOL

Iterator objects can be passed to the built-in
next()
function to fetch the next item

item = next(iterator)
'''

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)

next(iterator)  # Spring
next(iterator)  # Summer
next(iterator)  # Autumn
next(iterator)  # Winter
next(iterator)  # StopIteration Exception