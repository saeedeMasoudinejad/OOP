from address import Address
from residentail import Residential


class Apartment(Residential):
    def __init__(self, area, address, age, rooms, floor, elevator):
        self.floor = floor
        self.elevator = elevator
        return super(Residential).__init__(area=area, address=address, age=age, rooms=rooms)

    # def cal_unit_price(self):
    #     if self.address == Addres
