from tires.tires import Tires

class octoprime_tires(Tires):
    def __init__(self, wear_sensor_readings:list) -> None:
        self.wear_sensor_readings = wear_sensor_readings
    def needs_service(self):
        return sum(self.wear_sensor_readings) >= 3.0