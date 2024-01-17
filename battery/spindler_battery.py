from battery.battery import Battery
from utils import add_years

class spindler_battery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        next_service_date = add_years(self.last_service_date, 2)
        return next_service_date < self.current_date
