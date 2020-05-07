'''
    properties are descriptors

    Function decorators are regular functions which process an existing function and returns
        a new object (a new function which wraps the decorated function)

    THIS:
        @decorator
        def f():
            do_something()
    
    IS EQUAL TO THIS:
        def f():
            do_something()
        
        f = decorator(f)

    As decorators are functions, we change the code to avoid the duplication
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

    def _get_radius_meters(self):
        return self._radius_meters
    
    def _set_radius_meters(self, value):
        if value <= 0:
            raise ValueError("radius_meters value {} is not positive.".format(value))
        self._radius_meters = value
    
    radius_meters = property(fget=_get_radius_meters, 
                             fset=_set_radius_meters)                           # Using the decorator as a function 

    def _get_mass_kilograms(self):
        return self._mass_kilograms

    def _set_mass_kilograms(self, value):
        if value <= 0:
            raise ValueError("mass_kilograms value {} is not positive".format(value))
        self._mass_kilograms = value
    
    mass_kilograms = property(fget=_get_mass_kilograms, 
                              fset=_set_mass_kilograms)                         # Using the decorator as a function 

    def _get_orbital_period_seconds(self):
        return self._orbital_period_seconds
    
    def _set_orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError("orbital_period_seconds value {} is not positive".format(value))
        self._orbital_period_seconds = value

    orbital_period_seconds = property(fget=_get_orbital_period_seconds, 
                                      fset=_set_orbital_period_seconds)         # Using the decorator as a function 

    def _get_surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    def _set_surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError("surface_temperature_kelvin value {} is not positive".format(value))
        self._surface_temperature_kelvin = value
    
    surface_temperature_kelvin = property(fget=_get_surface_temperature_kelvin, 
                                          fset=_set_surface_temperature_kelvin) # Using the decorator as a function 

if __name__ == "__main__":
    
    # Trying to create a mass-less planet is not possible
    planet_x = Planet(name="X", radius_meters=10e3, mass_kilograms=0, orbital_period_seconds=7293234, 
                      surface_temperature_kelvin=-5)
                    # ValueError: mass_kilograms value 0 is not positive

    # The problem now is that the code expanded too much and has a lot of duplication 
    #   even with decorators as functions