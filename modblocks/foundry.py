"""Module for foundries."""

from .beacon import Beacon
from .crafting_station import BaseCraftingStation
from .recipe import Recipe

SPEED_BY_QUALITY = (4.0, 5.2, 6.4, 7.6, 10.0)


class Foundry(BaseCraftingStation):
    """Foundry class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Foundry."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.5
        self._module_slots: int = 4
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station."""
        return "Foundry"
