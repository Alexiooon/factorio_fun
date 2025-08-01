"""Module for furnace."""

from ..recipe import Recipe
from .beacon import Beacon
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (2.0, 2.6, 3.2, 3.8, 5.0)


class ElectricFurnace(BaseCraftingStation):
    """Electric furnace class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Electric furnace."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.0
        self._module_slots: int = 2
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station + recipe."""
        recipe = str(self.recipe) if self.recipe is not None else "Empty"
        return "Electric furnace: " + recipe
