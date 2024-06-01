from abc import ABCMeta, abstractmethod


class ITeslaBuilder(metaclass=ABCMeta):
    "Tesla vehicles interface"

    @staticmethod
    @abstractmethod
    def set_number_of_engines(number):
        "Number of Engines"

    @staticmethod
    @abstractmethod
    def set_chassis_type(model):
        "Chassis type"
    
    @staticmethod
    @abstractmethod
    def set_battery_type(range):
        "Battery type"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"