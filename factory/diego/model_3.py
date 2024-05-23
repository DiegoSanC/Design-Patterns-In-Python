from interface_tesla import EVTesla

class Model3(EVTesla):
    def __init__(self):
        self._battery_capacity = 60
        self._range = 554
        self._acceleration = 6.1
        
    def get_range(self):
        return self._range