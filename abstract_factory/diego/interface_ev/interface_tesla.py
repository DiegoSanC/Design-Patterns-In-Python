from abc import ABCMeta, abstractmethod

class EVTesla(metaclass=ABCMeta):
    "Tesla vehicle interface"
    
    @staticmethod
    @abstractmethod
    def create_vehicle(self):
        "interface method"