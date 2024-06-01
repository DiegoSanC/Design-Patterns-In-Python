from vehicles.tesla_model_3 import Model3
from vehicles.tesla_cybertruck import CyberTruck

class GigaFactoryAustin:
    @staticmethod
    def create_vehicle(type_):
        match type_:
            case 'model3':
                return Model3()
            case 'cybertruck':
                return CyberTruck() 
            case _:
                raise ValueError(f'Vehicle {type_} not found')
            

if __name__ == "__main__":
    factory = GigaFactoryAustin()
    semi = factory.create_vehicle('modelY')