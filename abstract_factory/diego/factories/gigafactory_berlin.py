from abstract_factory.diego.vehicles.tesla_model_y import ModelY

class GigaFactoryBerlin:
    @staticmethod
    def create_vehicle(type_):
        match type_:
            case 'modelY':
                return ModelY()
            case _:
                raise ValueError(f'Vehicle {type_} not found')
            

if __name__ == "__main__":
    factory = GigaFactoryBerlin()
    semi = factory.create_vehicle('modelY')