"""Module for Cryogenic plants."""

from ..recipe import Recipe
from .beacon import Beacon
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (2.0, 2.6, 3.2, 3.8, 5.0)


class CryogenicPlant(BaseCraftingStation):
    """Cryogenic plant class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Cryogenic plant."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.0
        self._module_slots: int = 8
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station."""
        return "Cryogenic plant"
