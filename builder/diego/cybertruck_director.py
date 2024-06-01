from tesla_builder import TeslaBuilder

class CyberTruckDirector:
    "CyberTruck Director"

    @staticmethod
    def construct():
        cybertruck = TeslaBuilder()
        cybertruck.set_chassis_type("CyberTruck")
        cybertruck.set_number_of_engines(2)
        cybertruck.set_battery_type("long range")
        return cybertruck.get_result()