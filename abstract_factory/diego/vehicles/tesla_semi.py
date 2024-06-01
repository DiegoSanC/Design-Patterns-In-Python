from interface_ev.interface_tesla import EVTesla

class Semi(EVTesla):
    def __init__(self):
        self._battery_capacity = 800
        self._range = 500
        self._acceleration = 20.0
        
    def create_vehicle(self):
        return self