from interface_tesla import EVTesla

class ModelS(EVTesla):
    def __init__(self):
        self._battery_capacity = 100
        self._range = 723
        self._acceleration = 3.2
        
    def get_range(self):
        return self._range