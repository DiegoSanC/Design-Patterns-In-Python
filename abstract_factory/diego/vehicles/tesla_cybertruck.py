from interface_ev.interface_tesla import EVTesla

class CyberTruck(EVTesla):
    def __init__(self):
        self._battery_capacity = 100
        self._range = 500
        self._acceleration = 2.9
        
    def create_vehicle(self):
        return self