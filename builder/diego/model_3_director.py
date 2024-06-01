from tesla_builder import TeslaBuilder

class Model3Director:
    "Model 3 Director"

    @staticmethod
    def construct():
        model_3 = TeslaBuilder()
        model_3.set_chassis_type("Model 3")
        model_3.set_number_of_engines(2)
        model_3.set_battery_type("long range")
        return model_3.get_result()