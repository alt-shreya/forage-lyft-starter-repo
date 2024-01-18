from tires.tires import Tires

class carrigan_tires(Tires):
    def __init__(self, wear_sensor_readings:list) -> None:
        self.wear_sensor_readings = wear_sensor_readings
    def needs_service(self):
        return 