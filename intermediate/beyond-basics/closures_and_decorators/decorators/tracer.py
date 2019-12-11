'''Use class instances as decoratos'''

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    print(l)
    l = rotate_list(l)
    print(l)
    l = rotate_list(l)
    print(l)
    print('disabling tracer')
    tracer.enabled = False
    l = rotate_list(l)
    print(l)