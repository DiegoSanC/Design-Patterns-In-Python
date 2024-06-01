from gigafactory_austin import GigaFactoryAustin
from gigafactory_fremont import GigaFactoryFremont
from interface_abstract_giga_factory import IAbstractGigaFactory

class AbstractGigaFactory(IAbstractGigaFactory):
    @staticmethod
    def create_vehicle(vehicle):
        match vehicle:
            case 'model3':
                return GigaFactoryAustin.create_vehicle('model3')
            case 'cybertruck':
                return GigaFactoryAustin.create_vehicle('cybertruck')
            case 'modelS':
                return GigaFactoryFremont.create_vehicle('modelS')
            case _:
                raise ValueError(f'Vehicle {vehicle} not valid')