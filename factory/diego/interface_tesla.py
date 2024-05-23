from abc import ABCMeta, abstractmethod

class EVTesla(metaclass=ABCMeta):
    "Tesla vehicle interface"
    
    @staticmethod
    @abstractmethod
    def get_range():
        "interface method"