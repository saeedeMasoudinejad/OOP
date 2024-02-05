from abc import ABC, abstractmethod

from property import Property


class Residential(Property):
    def __init__(self, area, address, age, rooms):
        self.age = age
        self.rooms = rooms
        return super().__init__(area, address)

    # @abstractmethod
    # def get

