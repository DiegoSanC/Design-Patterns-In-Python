class TeslaVehicle():
    def __init__(self) -> None:
        self._number_of_engines = None
        self._chassis_type = None
        self._battery_type = None
    
    @property
    def number_of_engines(self):
        return self._number_of_engines
    
    @number_of_engines.setter
    def number_of_engines(self, number):
        if number in [2, 4]:
            self._number_of_engines = number
        else:
            raise ValueError("Number of engines not valid")
    
    @property
    def battery_type(self):
        return self._battery_type
    
    @battery_type.setter
    def battery_type(self, range):
        if range in ["normal range", "long range"]:
            self._battery_type = range
        else:
            raise ValueError("Battery type not valid")
    
    @property
    def chassis_type(self):
        return self._chassis_type
    @chassis_type.setter
    def chassis_type(self, model):
        if model in ["Model S", "Model 3", "CyberTruck"]:
            self._chassis_type = model
        else:
            raise ValueError("Chassis type not valid")
    

    def construction(self):
        return f"This is a {self.number_of_engines} engine {self.chassis_type} with a {self.battery_type} battery."
