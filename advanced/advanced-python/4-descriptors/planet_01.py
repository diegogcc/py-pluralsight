'''
    properties are descriptors
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

if __name__ == "__main__":
    
    # Trying to create a mass-less planet shouldn't be possible
    planet_x = Planet(name="X", radius_meters=10e3, mass_kilograms=0, orbital_period_seconds=7293234, 
                      surface_temperature_kelvin=-5)