"""Module for chemical plants."""

from ..recipe import Recipe
from .beacon import Beacon
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (1.0, 1.3, 1.6, 1.9, 2.5)


class ChemicalPlant(BaseCraftingStation):
    """Chemical plant class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Chemical plant."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.0
        self._module_slots: int = 3
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station."""
        return "Chemical Plant"
