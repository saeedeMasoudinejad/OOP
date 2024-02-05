from abc import ABC, abstractmethod


class Property(ABC):
    def __init__(
            self,
            area,
            address):
        self.area = area
        self.address = address

        @abstractmethod
        def get_unit_price():
            raise NotImplementedError

        def calc_price(self):
            return self.get_unit_price() * self.area

        @abstractmethod
        def display_price(self):
            pass



