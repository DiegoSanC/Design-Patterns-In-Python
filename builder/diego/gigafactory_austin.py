from model_3_director import Model3Director
from cybertruck_director import CyberTruckDirector

class GigaFactoryAustin:
    @staticmethod
    def create_vehicle(type_):
        match type_:
            case 'model3':
                return Model3Director.construct()
            case 'cybertruck':
                return CyberTruckDirector.construct() 
            case _:
                raise ValueError(f'Vehicle {type_} not found')
            