'''
    Implement SLOTS:
        a mechanism to reduce memory usage
'''

class Resistor:

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


class SlotsResistor:

    __slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


if __name__ == "__main__":
    import sys

    r10 = Resistor(10, 5, 0.25)

    ''' size of instance of resistor = size of resistor object + size of its dict '''
    sys.getsizeof(r10) + sys.getsizeof(r10.__dict__)
    # 184

    r10.cost_dollars = 0.02
    # 0.02


    ''' size is now smaller but we cannot dynamically add attributes anymore 
            because now the object doesn't have a dict'''
    r11 = SlotsResistor(10, 5, 0.25)
    sys.getsizeof(r11) 
    # 72

    r11.cost_dollars = 0.02    
    # AttributeError: 'SlotsResistor' object has no attribute 'cost_dollars'