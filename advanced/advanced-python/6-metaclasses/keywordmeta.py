"""
                                        4
Example of overriding __call__
                # in charge of class allocation an initialization
"""

class KeywordOnlyMeta(type):
    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError("Constructor for class {!r} does not accept positional arguments.".format(cls))
        return super().__call__(cls, *args, **kwargs)

class ConstrainedToKeywords(metaclass=KeywordOnlyMeta):
    def __init__(self, *args, **kwargs):
        print("args = ", args)
        print("kwargs = ", kwargs)

if __name__ == "__main__":
    c = ConstrainedToKeywords(23, 45, 86, color='white')
    # TypeError: Constructor for class <class 'keywordmeta.ConstrainedToKeywords'> does not accept positional arguments.

    c = ConstrainedToKeywords(color='white')                  # only keyword arguments are allowed
    # args =  (<class 'keywordmeta.ConstrainedToKeywords'>,)
    # kwargs =  {'color': 'white'}