from abc import ABCMeta, abstractmethod

class IAbstractGigaFactory(metaclass=ABCMeta):
    "Abstrac Factory interface"
    
    @staticmethod
    @abstractmethod
    def create_vehicle(vehicle):
        "interface method"
    