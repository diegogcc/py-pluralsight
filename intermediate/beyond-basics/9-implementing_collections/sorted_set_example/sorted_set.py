from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain

class SortedSet(Sequence, Set):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    # ''' Implementation for the TestContainerProtocol '''
    # def __contains__(self, item):
    #     return item in self._items

    ''' Alternative/faster implementation of __contains__() '''
    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    ''' Implementation for the TestSizedProtocol '''
    def __len__(self):
        return len(self._items)

    ''' Implementation for the TestIterableProtocol '''
    def __iter__(self):
        return iter(self._items)

    ''' Alternative implementation of __iter__() '''
    # def __iter__(self):
    #     for item in self._items:
    #         yield item

    ''' Implementation for the TestSequenceProtocol '''
    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result 

    ''' Implementation for the TestReprProtocol '''
    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    ''' Implementation for the TestEqualityProtocol '''
    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    ''' Implementation for the TestInequalityProtocol '''
    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    ''' Implement index to be faster with a binary search '''
    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    ''' Implement count to be faster with a binary search '''
    def count(self, item):
        return int(item in self)
    
    ''' Implementation for the TestConcatenationProtocol '''
    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    ''' Implementation for the TestRepetitionProtocol '''
    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()    

    def __rmul__(self, lhs):
        return self * lhs       # <-- delegates to __mul__()

    ''' Implementation for the TestRelationalMethods '''
    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    ''' Implementation for the TestSetOperationsMethods '''
    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)