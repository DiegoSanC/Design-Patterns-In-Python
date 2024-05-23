from interface_tesla import EVTesla

class ModelY(EVTesla):
    def __init__(self):
        self._battery_capacity = 60
        self._range = 455
        self._acceleration = 6.9
        
    def get_range(self):
        return self._range
    