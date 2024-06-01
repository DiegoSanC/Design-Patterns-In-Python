from factories.gigafactory_nevada import GigaFactoryNevada
from factories.gigafactory_austin import GigaFactoryAustin
from factories.gigafactory_berlin import GigaFactoryBerlin
from interface_abstract_giga_factory import IAbstractGigaFactory

class AbstractGigaFactory(IAbstractGigaFactory):
    @staticmethod
    def create_vehicle(vehicle):
        match vehicle:
            case 'modelY':
                return GigaFactoryBerlin.create_vehicle('modelY')
            case 'model3':
                return GigaFactoryAustin.create_vehicle('model3')
            case 'cybertruck':
                return GigaFactoryAustin.create_vehicle('cybertruck')
            case 'semi':
                return GigaFactoryNevada.create_vehicle('semi')
            case _:
                raise ValueError(f'Vehicle {vehicle} not valid')
            

if __name__ == "__main__":
    PRODUCT = AbstractGigaFactory.create_vehicle('modelY')
    print(PRODUCT.__class__)