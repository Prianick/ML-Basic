from typing import Self
from .exceptions import LowFuelError, NotEnoughFuel

class Vehicle():
    def __init__(self, weight, fuel: float, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption # in liters per 100 km
        self._started = False

    @property
    def started(self) -> bool:
        return self._started

    @started.setter
    def started(self) -> Self:
        if(not self._started):
            if self.fuel <= 0:
                raise LowFuelError("Not enough fuel to start the vehicle.")
            self._started = True
        return self
    
    def _isEnoughFuel(self, distance: int) -> bool:
        required_fuel = (distance / 100) * self.fuel_consumption
        return self.fuel >= required_fuel

    def move(self, distance: int) -> Self:
        if self._isEnoughFuel(distance):
            self.fuel -= (distance / 100) * self.fuel_consumption
        else:
            raise NotEnoughFuel("Not enough fuel to move the vehicle.")
        return self
