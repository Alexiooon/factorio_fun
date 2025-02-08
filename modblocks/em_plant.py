"""Module for EM Plants."""
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (2.0, 2.6, 3.2, 3.8, 5.0)


class ElectromagneticPlant(BaseCraftingStation):
    """Electromagnetic plant class."""

    def __init__(self, quality: int):
        """Initialize a new Electromagnetic plant."""
        super().__init__()
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.5
        self._module_slots: int = 5
        self._modules = [None] * self._module_slots
