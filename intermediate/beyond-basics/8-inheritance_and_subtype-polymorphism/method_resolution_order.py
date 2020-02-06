''' 
    Method Resolution Order:
        ordering of a class' inheritance graph to determine
        which implementation to use when a method is invoked.

'''

class A:
    def func(self):
        return 'A.func'

class B(A):
    def func(self):
        return 'B.func'

class C(A):
    def func(self):
        return 'C.func'

class D(B, C):
    pass

if __name__ == "__main__":
    D.mro()
    # [
    # <class 'method_resolution_order.D'>, 
    # <class 'method_resolution_order.B'>, 
    # <class 'method_resolution_order.C'>, 
    # <class 'method_resolution_order.A'>, 
    # <class 'object'>
    # ]
    D.func()
    # 'B.func'