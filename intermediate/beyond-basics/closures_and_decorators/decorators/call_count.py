'''Use Class objects as decorators'''

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}'.format(name))

if __name__ == "__main__":
    hello('Diego')
    hello('Marco')
    hello('Lionel')
    print(hello.count)