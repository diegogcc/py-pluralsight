'''
    Non-Data descriptor:
        only implements __get__
        READ-ONLY
    
    Data descriptor:
        implements __get__, __set__ and/or __delete__
        WRITABLE

    Precedence of attribute lookup:
        object.__getattribute__         is responsible for all attribute lookup
            transforms:
                obj.attr
            into:
                type(obj).__dict__['attr'].__get__(obj, type(obj))
        if an instance's __dict__ has an entry with the same name as a DATA-DESCTIPTOR (get, set, delete)
            the data descriptor takes precedence 
        if an instance's __dict__ has an entry with the same name as a NON-DATA-DESCTIPTOR (get)
            the entry in __dict__ takes place 

        Precedence:
        1. data descriptor in class
        2. instance attribute in __dict__
        3. non-data descriptor in class

''' 

class DataDescriptor:
    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})".format(self, instance, owner))
    
    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})".format(self, instance, value))

class NonDataDescriptor:
    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})".format(self, instance, owner))


class Owner:
    a = DataDescriptor()
    b = NonDataDescriptor()


if __name__ == "__main__":
    obj = Owner()

    obj.a   # DataDescriptor.__get__(<__main__.DataDescriptor object at 0x11051d710>, <__main__.Owner object at 0x11051d910>, <class '__main__.Owner'>)
    
    obj.__dict__['a'] = 1234

    ''' since this is a data descriptor, the 1st rule applies and the data descriptor takes precedence '''
    obj.a   # DataDescriptor.__get__(<__main__.DataDescriptor object at 0x11051d710>, <__main__.Owner object at 0x11051d910>, <class '__main__.Owner'>)

    ''' since there are no entries with that name on __dict__, the non-data descriptor takes precedence (3rd rule) '''
    obj.b   # DataDescriptor.__get__(<__main__.NonDataDescriptor object at 0x11051d8d0>, <__main__.Owner object at 0x11051d910>, <class '__main__.Owner'>)

    ''' if we assign to that key on __dict__, instance attribute should take precedence (2nd rule) '''
    obj.__dict__['b'] = 5678
    obj.b   # 5678