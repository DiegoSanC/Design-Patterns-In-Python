from abstract_factory.diego.factories.gigafactory_nevada import GigaFactoryNevada
from abstract_factory.diego.factories.gigafactory_austin import GigaFactoryAustin
from abstract_factory.diego.factories.gigafactory_berlin import GigaFactoryBerlin
from abstract_factory.diego.interface_abstract_giga_factory import IAbstractGigaFactory

class AbstractGigaFactory(IAbstractGigaFactory):
    @staticmethod
    def create_giga_factory(vehicle):
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
    PRODUCT = AbstractGigaFactory.create_vehicle('cybertruck')
    print(PRODUCT.__class__)