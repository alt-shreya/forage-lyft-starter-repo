from battery.spindler_battery import spindler_battery
from battery.nubbin_battery import nubbin_battery

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tires.carrigan_tires import carrigan_tires
from tires.octoprime_tires import octoprime_tires

from car import Car

class car_factory():
    @staticmethod
    def Calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_readings):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        tires = carrigan_tires(wear_sensor_readings)
        return Car(engine, battery, tires)

    #  Ques: why do we use static method?

    @staticmethod
    def Glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_readings):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        tires = carrigan_tires(wear_sensor_readings)
        return Car(engine, battery, tires)

    @staticmethod
    def Palindrome(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_readings):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        tires = carrigan_tires(wear_sensor_readings)
        return Car(engine, battery, tires)

    @staticmethod
    def Rohrschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_readings):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        tires = octoprime_tires(wear_sensor_readings)
        return Car(engine, battery, tires) 

        
    @staticmethod
    def Thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_readings):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        tires = octoprime_tires(wear_sensor_readings)
        return Car(engine, battery, tires)    