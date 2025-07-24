from typing import Self
from .base import Vehicle
from .engine import Engine

class Car(Vehicle):
    """
    Car is a vehicle with an engine.
    """
    engine: Engine

    def set_engine(self, engine: Engine) -> Self:
        self.engine = engine
        return self