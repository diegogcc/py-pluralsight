'''
basic example
'''

class SimpleList:
    def __init__(self, items):
        self._items = list(items)
    
    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self): 
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


if __name__ == "__main__":
    sl = SortedList([4, 3, 78, 11])
    print(sl)
    # [3, 4, 11, 78]
    len(sl)     # 4
    sl.add(-42)
    print(sl)
    # [-42, 3, 4, 11, 78]

    il = IntList([1, 2, 3, 4])
    print(il)       # [1, 2, 3, 4]
    il.add(19)
    print(il)       # [1, 2, 3, 4, 19]
    il.add('5')     # TypeError

    issubclass(IntList, SimpleList)     # True
    issubclass(IntList, SortedList)     # False

    ''' Multiple inheritance '''
    sil = SortedIntList([1, 34, 12, 89, -2])
    # SortedIntList([-2, 1, 12, 34, 89])
    
    ''' MRO: Method Resolution Order '''
    SortedIntList.__mro__
    # (
    # <class 'sorted_list.SortedIntList'>, 
    # <class 'sorted_list.IntList'>, 
    # <class 'sorted_list.SortedList'>, 
    # <class 'sorted_list.SimpleList'>, 
    # <class 'object'>
    # )
    SortedIntList.mro()
    # [
    # <class 'sorted_list.SortedIntList'>, 
    # <class 'sorted_list.IntList'>, 
    # <class 'sorted_list.SortedList'>, 
    # <class 'sorted_list.SimpleList'>, 
    # <class 'object'>
    # ]