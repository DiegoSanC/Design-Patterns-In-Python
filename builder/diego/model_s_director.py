from tesla_builder import TeslaBuilder

class ModelSDirector:
    "Model S Director"

    @staticmethod
    def construct():
        model_s = TeslaBuilder()
        model_s.set_chassis_type("Model S")
        model_s.set_number_of_engines(4)
        model_s.set_battery_type("normal range")
        return model_s.get_result()
