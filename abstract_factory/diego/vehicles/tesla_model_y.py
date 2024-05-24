from abstract_factory.diego.interface_ev.interface_tesla import EVTesla

class ModelY(EVTesla):
    def __init__(self):
        self._battery_capacity = 60
        self._range = 455
        self._acceleration = 6.9
        
    def create_vehicle(self):
        return self
    