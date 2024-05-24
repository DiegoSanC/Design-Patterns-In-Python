from abstract_factory.diego.vehicles.tesla_semi import Semi

class GigaFactoryNevada:
    @staticmethod
    def create_vehicle(type_):
        match type_:
            case 'semi':
                return Semi()
            case _:
                raise ValueError(f'Vehicle {type_} not found')
            

if __name__ == "__main__":
    factory = GigaFactoryNevada()
    semi = factory.create_vehicle('semi')