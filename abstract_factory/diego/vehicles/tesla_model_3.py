from interface_ev.interface_tesla import EVTesla

class Model3(EVTesla):
    def __init__(self):
        self._battery_capacity = 75
        self._range = 322
        self._acceleration = 3.2
        
    def create_vehicle(self):
        return self