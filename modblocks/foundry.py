"""Module for foundries."""
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (4.0, 5.2, 6.4, 7.6, 10.0)


class Foundry(BaseCraftingStation):
    """Foundry class."""

    def __init__(self, quality: int):
        """Initialize a new Foundry."""
        super().__init__()
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.5
        self._module_slots: int = 4
        self._modules = [None] * self._module_slots
