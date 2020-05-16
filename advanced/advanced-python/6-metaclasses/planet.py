"""
                                        6
The original code comes from the Descriptor chapter. 
The problem there is that a descriptor doesn't have a way to know the class it has been bound to.
    this means that from the ValueError raised in __set__ when trying to set a negative number,
    we cannot know the attribute that we are modifying.
""" 

from weakref import WeakKeyDictionary

from tracing02 import TracingMeta

class Named:
    def __init__(self, name=None):
        self.name = name

class Positive(Named):
    def __init__(self, name=None):
        super().__init__(name)
        self._instance_data = WeakKeyDictionary()
    
    def __get__(self, instance, owner):
        return self._instance_data[instance]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Atribute value {} {} is not positive".format(self.name, value))
        self._instance_data[instance] = value 

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute {}".format(self.name))

class DescriptorNamingMeta(type):               # so we can detect the presence of descriptors which are named.
    def __new__(mcs, name, bases, namespace):
        for name, attr in namespace.items():
            if isinstance(attr, Named):
                attr.name = name 
        return super().__new__(mcs, name, bases, namespace)

class TracingDescriptorNamingMeta(TracingMeta, DescriptorNamingMeta):
    pass

class Planet(metaclass=TracingDescriptorNamingMeta):
    def __init__(self, 
                 name,
                 radius_meters,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
        self.name = name
        self.radius_meters = radius_meters
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value

    # Binding an instance of the Positive descriptor to a class attribute of the Planet
    radius_meters = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()

def make_planets():

    mercury = Planet("Mercury",
                     radius_meters=2439.7e3,
                     mass_kilograms=3.3022e23,
                     orbital_period_seconds=7.60052e6,
                     surface_temperature_kelvin=340)

    venus = Planet("Venus",
                   radius_meters=6051.8e3,
                   mass_kilograms=4.8676e24,
                   orbital_period_seconds=1.94142e7,
                   surface_temperature_kelvin=737)

    earth = Planet("Earth",
                   radius_meters=6371.0e3,
                   mass_kilograms=5.972e24,
                   orbital_period_seconds=3.15581e7,
                   surface_temperature_kelvin=288)

    mars = Planet("Mars",
                  radius_meters=3389.5e3,
                  mass_kilograms=6.4185e23,
                  orbital_period_seconds=5.93543e7,
                  surface_temperature_kelvin=210)

    return mercury, venus, earth, mars

if __name__ == "__main__":
    mercury, venus, earth, mars = make_planets()

    print(mercury.mass_kilograms)       # 3.3022e+23

    # Now we can see the name of the attribute 

    mercury.mass_kilograms = -100000
    # ValueError: Atribute value mass_kilograms -10000 is not positive
