'''
    properties are descriptors

    the @property decorator on a getter creates a property object
    the getter function is bound to the 'fget' attribute of the property object 

    the property object has a setter method (which is also a decorator)
    the 'fset' attribute of the property object is bound to the setter function
'''

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
    
    @property
    def radius_meters(self):
        return self._radius_meters
    
    @radius_meters.setter
    def radius_meters(self, value):
        if value <= 0:
            raise ValueError("radius_meters value {} is not positive.".format(value))
        self._radius_meters = value
    
    @property
    def mass_kilograms(self):
        return self._mass_kilograms

    @mass_kilograms.setter
    def mass_kilograms(self, value):
        if value <= 0:
            raise ValueError("mass_kilograms value {} is not positive".format(value))
        self._mass_kilograms = value

    @property
    def orbital_period_seconds(self):
        return self._orbital_period_seconds
    
    @orbital_period_seconds.setter
    def orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError("orbital_period_seconds value {} is not positive".format(value))
        self._orbital_period_seconds = value

    @property
    def surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    @surface_temperature_kelvin.setter
    def surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError("surface_temperature_kelvin value {} is not positive".format(value))
        self._surface_temperature_kelvin = value

if __name__ == "__main__":
    
    # Trying to create a mass-less planet is not possible
    planet_x = Planet(name="X", radius_meters=10e3, mass_kilograms=0, orbital_period_seconds=7293234, 
                      surface_temperature_kelvin=-5)
                    # ValueError: mass_kilograms value 0 is not positive

    # The problem now is that the code expanded too much and has a lot of duplication 