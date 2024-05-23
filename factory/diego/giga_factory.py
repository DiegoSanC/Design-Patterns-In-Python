from model_3 import Model3
from model_s import ModelS
from model_y import ModelY


class GigaFactory:
    
    @staticmethod
    def get_tesla(model):
        match model:
            case '3':
                return Model3()
            case 'S':
                return ModelS()
            case 'Y':
                return ModelY()
            case _:
                return None
            
            