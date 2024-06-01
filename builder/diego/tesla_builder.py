from interface_tesla_builder import ITeslaBuilder
from tesla_vehicle import TeslaVehicle

class TeslaBuilder(ITeslaBuilder):
    "Tesla Builder"

    def __init__(self):
        self.tesla = TeslaVehicle()

    def set_number_of_engines(self, number):
        self.tesla.number_of_engines = number
        return self

    def set_chassis_type(self, model):
        self.tesla.chassis_type = model
        return self

    def set_battery_type(self, range):
        self.tesla.battery_type = range
        return self

    def get_result(self):
        return self.tesla
