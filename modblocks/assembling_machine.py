"""Module for assembling machines."""
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (1.25, 1.625, 2.0, 2.375, 3.125)


class AssemblingMachine(BaseCraftingStation):
    """Assembling Machine 3 class."""

    def __init__(self, quality: int):
        """Initialize a new Assembling Machine 3."""
        super().__init__()
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.5
        self._module_slots: int = 4
        self._modules = [None] * self._module_slots
