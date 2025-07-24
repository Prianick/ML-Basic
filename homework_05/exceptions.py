class LowFuelError(Exception):
    """Exception raised when the vehicle has low fuel."""
    pass

class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass