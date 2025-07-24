from typing import Self
from .base import Vehicle
from .exceptions import CargoOverload

class Plane(Vehicle):
    cargo: float = 0.0  # in kg
    max_cargo: float = 10000.0  # maximum cargo capacity in kg

    def __init__(self, max_cargo: float):
        self.max_cargo = max_cargo

    def load_cargo(self, weight: float) -> Self:
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload("Cargo overload: cannot load more than maximum capacity.")
        self.cargo += weight
        return self

    def remove_all_cargo(self) -> float:
        tmp = self.cargo
        self.cargo = 0.0
        return tmp

