from model_s_director import ModelSDirector

class GigaFactoryFremont:
    @staticmethod
    def create_vehicle(type_):
        match type_:
            case 'modelS':
                return ModelSDirector.construct()
            case _:
                raise ValueError(f'Vehicle {type_} not found')