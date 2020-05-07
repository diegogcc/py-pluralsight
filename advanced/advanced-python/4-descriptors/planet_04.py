'''
    Implementing a descriptor:
        A class that implements the Descriptor protocol:
            __set__(), 
            __get__(), 
            __delete__()
'''

from weakref import WeakKeyDictionary

class Positive:
    def __init__(self):
        self._instance_data = WeakKeyDictionary()
    
    def __get__(self, instance, owner):
        return self._instance_data[instance]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value {} is not positive".format(value))
        self._instance_data[instance] = value 

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")

class Planet:
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

if __name__ == "__main__":
    
    pluto = Planet(name='Pluto', radius_meters=1184e3, mass_kilograms=1.305e22,
                   orbital_period_seconds=7816012992, surface_temperature_kelvin=55)

    ''' How does the descriptor works '''
    # m = pluto.mass_kilograms
    # m2 = Positive.__get__(self, pluto, Planet)
    #                           ^instance
    #                                  ^owner

    # The dictionaries created include the value for the same attribute of different instances 
    #       instead of having values for all attributes of only one instance. 

    mercury = Planet(name='Mercury', radius_meters=239.7e3, mass_kilograms=3.3022e23,
                     orbital_period_seconds=7.60052e6, surface_temperature_kelvin=340)
                    
    venus = Planet("Venus", radius_meters=6051.8e3, mass_kilograms=4.8676e24,
                   orbital_period_seconds=1.94142e7, surface_temperature_kelvin=737)

    earth = Planet("Earth", radius_meters=6371.0e3, mass_kilograms=5.972e24,
                   orbital_period_seconds=3.15581e7, surface_temperature_kelvin=288)

    mars = Planet("Mars", radius_meters=3389.5e3, mass_kilograms=6.4185e23,
                  orbital_period_seconds=5.93543e7, surface_temperature_kelvin=210)

    # When the instance of 'mars' is being created and the setter is used to save the values of the instance,
    #   the 'radius_meters' dictionary will already have values for all the radius of the other instances. 