'''
class Foo:
    a_class_attribute = 0
    def __init__(self):
        self.an_instance_attribute = 42
        Foo.a_class_attribute = 64

Instance attributes:
    self.owner_code   <- belongs to the instance

Class attibutes:
    ShippingContainer.next_serial   <- belongs to the class

@staticmethod -> can be overwritten in subclasses (inheritance)
@classmethod  -> defined in class will be inherited in subclass
'''
import iso6346

class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337                  # Class attribute

    @staticmethod
    def _get_next_serial():
        result =  ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod                        # Similar to @staticmethod
    def _get_next_serial_cls(cls):      # better usage when need to refer to the class object
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod                        # Named constructor / Factory function
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        # Named constructor:  constructs objects with certain configurations
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(owner_code=owner_code,
                    serial=ShippingContainer._get_next_serial())

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_ft3(self):
        return self._calc_volume()


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    FRIDGE_VOLUME_FT3 = 100    

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                    serial=str(serial).zfill(6), category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(farenheit):
        return (farenheit - 32) * 5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    @property
    def farenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return (super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3)


class HeatedRegrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRegrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature out of range")
        super()._set_celsius(value)


if __name__ == "__main__":
    c1 = ShippingContainer("YML", "books")
    print(c1.bic)           # YMLU0013374
    print(c1.contents)      # books
    c2 = ShippingContainer("MAE", "clothes")
    print(c2.bic)           # MAEU0013387
    print(c2.contents)      # clothes
    r1 = RefrigeratedShippingContainer('FSH', 'seafood', celsius=2.5)
    print(r1.bic)           # FSHR0013390
    print(r1.contents)      # seafood

    r2 = RefrigeratedShippingContainer.create_empty('YML', celsius=2.0)
    print(r2.celsius)       # 2.0
    # r2.celsius = 1.0      # AttributeError: can't set attribute without the setter
    r2._celsius = 1.0
    # r2._celsius = 5.0     # ValueError: Temperature too hot!