class ExampleIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()
        rslt = self.data[self.index]
        self.index += 1
        return rslt


class ExampleIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return ExampleIterator(self.data)


if __name__ == "__main__":
    i = ExampleIterator([1, 2, 3])
    next(i)
    # 1
    next(i)
    # 2
    next(i)
    # 3
    next(i)
    # StopIteration

    for i in ExampleIterator([1, 2, 3]):
        print(i)
    # 1
    # 2
    # 3

    for i in ExampleIterable():
        print(i)
    # 1
    # 2
    # 3

    [i * 3 for i in ExampleIterable()]
    # [3, 6, 9]